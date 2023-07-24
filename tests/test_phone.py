import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("Test Phone", 10, 5, 2)


def test_init(phone):
    assert phone.number_of_sim == 2


def test_repr(phone):
    assert repr(phone) == "Phone('Test Phone', 10, 5, 2)"


def test_number_of_sim(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
