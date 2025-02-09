import pytest

from src.classes import Product


@pytest.fixture()
def class_product_fixture() -> Product:
    return Product(
        aname="test_product", adescription="test_description", aprice=10.5, aquantity=10
    )


def test_class_init(class_product_fixture: Product) -> None:
    assert class_product_fixture.name == "test_product"
    assert class_product_fixture.description == "test_description"
    assert class_product_fixture.price == 10.5
    assert class_product_fixture.quantity == 10
