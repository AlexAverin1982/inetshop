import pytest

from src.classes import Category, Product


@pytest.fixture()
def class_product_fixture() -> Product:
    return Product(
        name="test_product", description="test_description", price=10.5, quantity=10
    )


@pytest.fixture()
def class_category_fixture() -> Category:
    return Category(name="test_category", description="test_description")


@pytest.fixture()
def three_products() -> list[Product]:
    prod1 = Product(name="prod1", quantity=10, price=100.0)
    prod2 = Product(name="prod2", quantity=10, price=100.0)
    prod3 = Product(name="prod3", quantity=10, price=100.0)
    return [prod1, prod2, prod3]
