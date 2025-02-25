from src.classes import Order, Product


def test_order_init(class_product_fixture: Product) -> None:
    """
    Тестируем создание заказа
    :param class_product_fixture: фикстура продукта в заказе
    :return:
    """
    prod_count = 5
    order = Order(class_product_fixture, prod_count)
    assert order.product.name == class_product_fixture.name
    assert order.count == prod_count


def test_add_product(three_products: list[Product]) -> None:
    """
    Тестируем редактирование заказа
    :param three_products: список продуктов для выбора: первый выбираем при создании заказа,
    второй - при редактировании
    :return:
    """
    old_count = Order.overall_count  # предыдущее число заказов
    order = Order(three_products[0], 1)
    prod_count = 5
    order.add_product(three_products[1], prod_count)
    assert order.product.name == three_products[1].name
    assert order.count == prod_count
    assert Order.overall_count == old_count + 1


def test_str(class_product_fixture: Product) -> None:
    """
    тестируем строковое представление заказа
    :param class_product_fixture: фикстура продукта в заказе
    :return:
    """
    prod_count = 5
    order = Order(class_product_fixture, prod_count)
    assert (
        str(order)
        == f"{class_product_fixture.name}: {class_product_fixture.price} * {order.count} = {order.total}"
    )
