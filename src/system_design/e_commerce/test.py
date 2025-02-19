from fastapi import FastAPI, Depends
from pydantic import BaseModel, UUID4
from typing import List
import uuid
import pika
import json
from threading import Thread
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, index=True)
    items = Column(String)
    total_price = Column(Float)
    status = Column(String, default="pending")

Base.metadata.create_all(bind=engine)

# Domain Layer
class OrderStatus:
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

class Order(BaseModel):
    id: UUID4
    items: List[str]
    total_price: float
    status: str = OrderStatus.PENDING

# Application Layer
class OrderService:
    def __init__(self, message_broker, repository):
        self.repository = repository
        self.message_broker = message_broker
    
    def create_order(self, items: List[str], total_price: float) -> Order:
        order = Order(id=uuid.uuid4(), items=items, total_price=total_price)
        self.repository.save_order(order)
        self.message_broker.publish("order.created", order.dict())
        return order
    
    def get_order(self, order_id: UUID4) -> Order:
        return self.repository.get_order(order_id)

# Infrastructure Layer - RabbitMQ
class RabbitMQBroker:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="order_events")
    
    def publish(self, event: str, data: dict):
        message = json.dumps({"event": event, "data": data})
        self.channel.basic_publish(exchange="", routing_key="order_events", body=message)
    
    def consume(self, callback):
        def _callback(ch, method, properties, body):
            message = json.loads(body)
            callback(message["event"], message["data"])
        
        self.channel.basic_consume(queue="order_events", on_message_callback=_callback, auto_ack=True)
        self.channel.start_consuming()

# Infrastructure Layer - Repository
class OrderRepository:
    def __init__(self):
        self.db = SessionLocal()
    
    def save_order(self, order: Order):
        db_order = OrderDB(id=str(order.id), items=",".join(order.items), total_price=order.total_price, status=order.status)
        self.db.add(db_order)
        self.db.commit()
    
    def get_order(self, order_id: UUID4) -> Order:
        db_order = self.db.query(OrderDB).filter(OrderDB.id == str(order_id)).first()
        if db_order:
            return Order(id=db_order.id, items=db_order.items.split(","), total_price=db_order.total_price, status=db_order.status)
        return None

# API Layer
app = FastAPI()
repository = OrderRepository()
message_broker = RabbitMQBroker()
order_service = OrderService(message_broker, repository)

class CreateOrderRequest(BaseModel):
    items: List[str]
    total_price: float

@app.post("/orders", response_model=Order)
def create_order(request: CreateOrderRequest):
    return order_service.create_order(request.items, request.total_price)

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: UUID4):
    order = order_service.get_order(order_id)
    if not order:
        return {"error": "Order not found"}
    return order

# Start RabbitMQ Consumer in a separate thread
def start_consumer():
    def handle_event(event, data):
        print(f"Received event: {event} with data: {data}")
    
    message_broker.consume(handle_event)

consumer_thread = Thread(target=start_consumer, daemon=True)
consumer_thread.start()
