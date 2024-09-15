from sqlalchemy import text
from src.domain_driven_design.cosmic_python.app.domain.entities.order_line import OrderLine


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        text(
            "INSERT INTO order_lines (order_id, sku, qty) VALUES "
            '("order1", "RED-CHAIR", 12),'
            '("order1", "RED-TABLE", 13),'
            '("order2", "BLUE-LIPSTICK", 14)'
            )
        )
    expected = [
        OrderLine("order1", "RED-CHAIR", 12),
        OrderLine("order1", "RED-TABLE", 12),
        OrderLine("order2", "BLUE-LIPSTICK", 12)
    ]
    assert session.query(OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(new_line)
    session.commit()
    rows = list(session.execute(
        text('SELECT order_id, sku, qty FROM "order_lines"')
    ))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]
