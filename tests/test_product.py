import pytest

import src.classes
from src.classes import Product


def test_class_init(class_product_fixture: Product) -> None:
    assert class_product_fixture.name == "test_product"
    assert class_product_fixture.description == "test_description"
    assert class_product_fixture.price == 10.5
    assert class_product_fixture.quantity == 10


def test_new_product(three_products: list[Product]) -> None:
    cur_quantity = three_products[0].quantity
    new_quantity = 1
    name = three_products[0].name
    new_product = Product.new_product(
        {"name": name, "quantity": new_quantity}, existing_products=three_products
    )
    assert (new_product == three_products[0]) and (
            new_product.quantity == cur_quantity + new_quantity
    )


def test_new_product2(three_products: list[Product]) -> None:
    cur_quantity = three_products[0].quantity
    new_quantity = 1
    new_product = Product.new_product('blahblah')
    assert (new_product.name == 'noname')


def test_new_product3(three_products: list[Product]) -> None:
    old_price = three_products[0].price
    name = three_products[0].name
    new_product = Product.new_product({"name": name, "price": old_price * 1.2}, existing_products=three_products)
    assert (new_product == three_products[0]) and (three_products[0].price == old_price * 1.2)


def test_new_price(three_products: list[Product]) -> None:
    old_price = three_products[0].price
    three_products[0].price *= 10
    assert three_products[0].price == old_price * 10


def test_new_product3(three_products: list[Product]) -> None:
    cur_quantity = three_products[0].quantity
    new_quantity = 100
    new_price = 999999.9
    new_product = Product.new_product(
        {"name": "prod1", "quantity": new_quantity, 'price': new_price}, existing_products=three_products
    )
    assert (new_product == three_products[0]) and (
            new_product.quantity == cur_quantity + new_quantity
    )


def test_lower_price(three_products: list[Product]) -> None:
    def mock_input(prompt: str) -> str:
        return "y"

    src.classes.input = mock_input
    old_price = three_products[0].price
    new_price = old_price * 0.8
    three_products[0].price = new_price
    assert three_products[0].price == new_price


def test_negative_price(three_products: list[Product]) -> None:
    output = []
    src.classes.print = lambda s: output.append(s)
    old_price = three_products[0].price
    three_products[0].price = -three_products[0].price
    assert (three_products[0].price == old_price) and (
            output[-1] == "Цена не должна быть нулевая или отрицательная"
    )
