# mypy: disable-error-code="attr-defined"
import tests.aux_subs
from src.classes import Product, Order, Category


def test_adding_zero_products_to_category(
    class_category_fixture: Category, three_products: list[Product]
) -> None:
    # перенаправляем тестовый вывод в консоль для проверки вывода тестовой информации
    # о добавлении продкуктов в категорию
    output = []
    tests.aux_subs.print = lambda s: output.append(s)

    tests.aux_subs.try_adding_zero_products(
        class_category_fixture, three_products, [1, 0, 1]
    )
    assert output[-1] == output[-3] == output[-5] == "Добавление товара завершено"
    assert (
        output[-6]
        == f"Товар {three_products[0].name} добавлен в категорию успешно в количестве 1 шт."
    )
    assert (
        output[-4]
        == f"Товар {three_products[1].name} с нулевым количеством не может быть добавлен"
    )
    assert (
        output[-2]
        == f"Товар {three_products[2].name} добавлен в категорию успешно в количестве 1 шт."
    )


def test_adding_zero_products_to_order(
    class_order_fixture: Order, three_products: list[Product]
) -> None:
    # перенаправляем тестовый вывод в консоль для проверки вывода тестовой информации
    # о добавлении продкуктов в категорию
    output = []
    tests.aux_subs.print = lambda s: output.append(s)

    tests.aux_subs.try_ordering_zero_products(
        class_order_fixture, three_products, [1, 0, 1]
    )
    assert (
        output[-1] == output[-3] == output[-5] == "Добавление товара в заказ завершено"
    )
    assert (
        output[-6]
        == f"Товар {three_products[0].name} добавлен в заказ успешно в количестве 1 шт."
    )
    assert (
        output[-4]
        == f"Товар {three_products[1].name} с нулевым количеством не может быть добавлен в заказ."
    )
    assert (
        output[-2]
        == f"Товар {three_products[2].name} добавлен в заказ успешно в количестве 1 шт."
    )
