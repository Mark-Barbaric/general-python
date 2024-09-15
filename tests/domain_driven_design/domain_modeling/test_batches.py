from datetime import date
from src.domain_driven_design.cosmic_python.domain_modeling.model import Batch, OrderLine


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)
    assert large_batch.available_quantity == 20
    assert large_batch.allocate(small_line)
    assert large_batch.available_quantity == 18


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert not small_batch.can_allocate(large_line)


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)
    assert batch.allocate(line)
    assert not batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert not batch.can_allocate(different_sku_line)


def test_can_only_deallocated_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    assert not batch.deallocate(unallocated_line)
    batch.allocate(unallocated_line)
    assert batch.available_quantity == 18
    assert batch.deallocate(unallocated_line)
