from src.classes import Category, CategoryMeta, Product


def test_total_cost(three_products: list[Product]) -> None:
    cat = Category(name="cat1", description="test cat", products=three_products)
    cm = CategoryMeta(category=cat)
    expected_result = 0.0
    for prod in three_products:
        expected_result += prod.quantity * prod.price

    assert cm.get_total_cost() == expected_result
    assert cm.get_total_cost() == expected_result
