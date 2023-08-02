import pytest
from src.items import Item


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
    assert repr(item) == "Item('Test Item', 10, 5)"


def test_str(item):
    assert str(item) == "Test Item"


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Телефон", 5000, 10)
    assert (item1 + item2) == 30
    assert (item1 + 10000) == None


def test_instantiate_from_csv_FileNotFoundError():
    assert Item.instantiate_from_csv('test3.csv') == 'Отсутствует файл items.csv'


def test_instantiate_from_csv_InstantiateCSVError():
    assert Item.instantiate_from_csv('test4.csv') == 'Файл items.csv поврежден'
