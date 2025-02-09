import pytest
from src.classes import Product


@pytest.fixture()
def test_class_Product():
    return Product()


