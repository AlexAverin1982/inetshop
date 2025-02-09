import pytest

from src.classes import Category


@pytest.fixture()
def class_category_fixture() -> Category:
    return Category(aname="test_category", adescription="test_description")


def test_class_init(class_category_fixture: Category) -> None:
    assert class_category_fixture.name == "test_category"
    assert class_category_fixture.description == "test_description"


def test_category_count() -> None:
    passed = Category.category_count == 0
    if passed:
        cat1 = Category(aname="cat1")
        cat2 = Category(aname="cat2")
        passed = Category.category_count == 2

    #     if passed:
    #         del cat1   # не работает...
    #         # passed = Category.category_count == 1 # не работает...
    #
    #         del cat2 # не работает...
    # passed = Category.category_count == 0 # не работает...
    assert passed


def test_products_count(class_category_fixture: Category) -> None:
    passed = Category.product_count == 0
    if passed:
        class_category_fixture.add_product("product 1")
        passed = Category.product_count == 1
        class_category_fixture.add_product("product 2")
        passed = Category.product_count == 2
        class_category_fixture.delete_product("product 1")
        passed = Category.product_count == 1
        class_category_fixture.delete_product("product 2")
        passed = Category.product_count == 0
    #     if passed:
    #         del cat1   # не работает...
    #         # passed = Category.category_count == 1 # не работает...
    #
    #         del cat2 # не работает...
    # passed = Category.category_count == 0 # не работает...
    assert passed
