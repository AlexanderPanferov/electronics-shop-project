import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Test Item", 10, 5)


def test_init(item):
    assert item.name == "Test Item"
    assert item.price == 10
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10


def test_string_to_number():
    assert Item.string_to_number('5.0') == 5


def test_repr(item):
    assert repr(item) == 'Item("Test Item", 10, 5)'


def test_str(item):
    assert str(item) == "Test Item"
