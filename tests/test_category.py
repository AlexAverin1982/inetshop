import pytest

from src.classes import Category, Product


def test_class_init(class_category_fixture: Category) -> None:
    assert class_category_fixture.name == "test_category"
    assert class_category_fixture.description == "test_description"


def test_category_count() -> None:
    passed = Category.category_count == 0
    if passed:
        cat1 = Category(name="cat1")
        cat2 = Category(name="cat2")
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


def test_add_products_in_constructor() -> None:
    prod1 = Product(name="prod1")
    prod2 = Product(name="prod2")
    cat = Category(name="cat", description="desc", products=[prod1, prod2])
    assert Category.product_count == 2


def test_print_products(three_products: list[Product]) -> None:
    # output = []
    # src.classes.print = lambda s: output.append(s)
    cat = Category(name="new cat", description="test desc", products=three_products)

    line0 = f"{three_products[0].name}, {three_products[0].price} руб. Остаток: {three_products[0].quantity} шт."
    line1 = f"{three_products[1].name}, {three_products[1].price} руб. Остаток: {three_products[1].quantity} шт."
    line2 = f"{three_products[2].name}, {three_products[2].price} руб. Остаток: {three_products[2].quantity} шт."
    assert cat.products == "\n".join([line0, line1, line2])


def test_add_some_unknown_stuff():
    cat = Category(name="new cat", description="test desc")
    cat.add_product("blahblah")
    assert cat.get_product_by_index(-1).name == 'blahblah'


def test_add_product_product(class_product_fixture):
    cat = Category(name='cat1')
    cat.add_product(class_product_fixture)
    assert (class_product_fixture == cat.get_product_by_index(-1)) and \
           (class_product_fixture == cat.get_product_by_index(0))


def test_get_by_index_out_of_bounds(class_category_fixture):
    assert (class_category_fixture.get_product_by_index(10) is None)
