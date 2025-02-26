"""
вспомогательные подпрограммы для тестирования функционала классов на предмет контроля ошибок
"""

from src.classes import Category, Order, Product
from src.custom_exceptions import ZeroProductQuantityException


def try_adding_zero_products(
    category: Category, products: list[Product], counts: list[int]
) -> None:
    """
    проверяем, как будут в категорию добавляться продукты с нулевым количеством
    """
    for product, count in zip(products, counts):
        try:
            category.add_product(product, count)
        except ZeroProductQuantityException:
            print(f"Товар {product.name} с нулевым количеством не может быть добавлен")
        else:
            print(
                f"Товар {product.name} добавлен в категорию успешно в количестве {count} шт."
            )
        finally:
            print("Добавление товара завершено")


def try_ordering_zero_products(
    order: Order, products: list[Product], counts: list[int]
) -> None:
    """
    проверяем, как будут в заказ добавляться продукты с нулевым количеством
    """
    for product, count in zip(products, counts):
        try:
            order.add_product(product, count)
        except ZeroProductQuantityException:
            print(
                f"Товар {product.name} с нулевым количеством не может быть добавлен в заказ."
            )
        else:
            print(
                f"Товар {product.name} добавлен в заказ успешно в количестве {count} шт."
            )
        finally:
            print("Добавление товара в заказ завершено")
