from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import registry, relationship
from ..domain.entities import order_line


mapper_registry = registry()


order_lines_table = Table(
    "order_lines",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255), nullable=False),
    Column("qty", Integer, nullable=False),
    Column("order_id", String(255), nullable=False)
)

batches_tables = Table(
    "batches",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", String(255)),
    Column("purchased_quantity", Integer, nullable=False),
    Column("eta", Date, nullable=False)
)

allocations_table = Table(
    "allocations",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_line_id", ForeignKey("order_lines.id")),
    Column("batch_id", ForeignKey("batches.id"))
)


def start_mappers():
    lines_mapper = mapper_registry.map_imperatively(order_line.OrderLine, order_lines_table)
    mapper_registry.map_imperatively(
        order_line.Batch,
        batches_tables,
        properties = {
            "allocations": relationship(
                lines_mapper,
                secondary=allocations_table,
                collection_class=set
            )
        }
    )