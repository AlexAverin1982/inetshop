import pytest

from src.classes import Category, Product


def test_class_init(class_category_fixture: Category) -> None:
    assert class_category_fixture.name == "test_category"
    assert class_category_fixture.description == "test_description"


def test_category_count() -> None:
    prev_count = Category.category_count
    cat1 = Category(name="cat1")
    cat2 = Category(name="cat2")
    passed = Category.category_count == prev_count + 2

    #     if passed:
    #         del cat1   # не работает...
    #         # passed = Category.category_count == 1 # не работает...
    #
    #         del cat2 # не работает...
    # passed = Category.category_count == 0 # не работает...
    assert passed


def test_products_count(
    class_category_fixture: Category, three_products: list[Product]
) -> None:
    old_count = Category.product_count
    class_category_fixture.add_product(three_products[0])
    passed = Category.product_count == old_count + 1
    class_category_fixture.add_product(three_products[1])
    passed = Category.product_count == old_count + 2
    class_category_fixture.add_product(three_products[2])
    passed = Category.product_count == old_count + 3
    # class_category_fixture.delete_product("product 2")
    # passed = Category.product_count == old_count + 0
    #     if passed:
    #         del cat1   # не работает...
    #         # passed = Category.category_count == 1 # не работает...
    #
    #         del cat2 # не работает...
    # passed = Category.category_count == 0 # не работает...
    assert passed


def test_add_products_in_constructor() -> None:
    old_count = Category.product_count
    prod1 = Product(name="prod1")
    prod2 = Product(name="prod2")
    cat = Category(name="cat", description="desc", products=[prod1, prod2])
    assert Category.product_count == old_count + 2


def test_print_products(three_products: list[Product]) -> None:
    # output = []
    # src.classes.print = lambda s: output.append(s)
    cat = Category(name="new cat", description="test desc", products=three_products)

    line0 = f"{three_products[0].name}, {three_products[0].price} руб. Остаток: {three_products[0].quantity} шт."
    line1 = f"{three_products[1].name}, {three_products[1].price} руб. Остаток: {three_products[1].quantity} шт."
    line2 = f"{three_products[2].name}, {three_products[2].price} руб. Остаток: {three_products[2].quantity} шт."
    assert cat.products == "\n".join([line0, line1, line2])


def test_add_some_unknown_stuff() -> None:
    cat = Category(name="new cat", description="test desc")
    with pytest.raises(TypeError):
        cat.add_product("blahblah")


def test_add_product_product(class_product_fixture: Product) -> None:
    cat = Category(name="cat1")
    cat.add_product(class_product_fixture)
    assert (class_product_fixture == cat.get_product_by_index(-1)) and (
        class_product_fixture == cat.get_product_by_index(0)
    )


def test_get_by_index_out_of_bounds(class_category_fixture: Category) -> None:
    assert class_category_fixture.get_product_by_index(10) is None


def test_get_products_count(three_products: list[Product]) -> None:
    cat = Category(name="new cat", description="test desc", products=three_products)
    assert cat.get_products_count() == 30


def test_add_non_product(three_products: list[Product]) -> None:
    cat = Category(name="new cat", description="test desc", products=three_products)
    with pytest.raises(TypeError):
        cat.add_product("Not a product")
