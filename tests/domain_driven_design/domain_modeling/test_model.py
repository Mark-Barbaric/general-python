from src.domain_driven_design.cosmic_python.domain_modeling.model import OrderLine


def test_order_line_comparison():
    order_line_1 = OrderLine("ORD0001", "T-SHIRT", 100)
    order_line_2 = OrderLine("ORD0001", "T-SHIRT", 200)
    order_line_3 = OrderLine("ORD0002", "T-SHIRT", 100)
    assert order_line_1 == order_line_2
    assert order_line_2 != order_line_3
    assert order_line_1 != order_line_3
