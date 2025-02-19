import pytest

import src.classes
from src.classes import LawnGrass, Smartphone


def test_class_init(class_smartphone_fixture: Smartphone) -> None:
    assert class_smartphone_fixture.name == "test_smartphone"
    assert class_smartphone_fixture.description == "test_description"
    assert class_smartphone_fixture.price == 10.5
    assert class_smartphone_fixture.quantity == 10
    assert class_smartphone_fixture.efficiency == 1000.0
    assert class_smartphone_fixture.model == "Iphone999"
    assert class_smartphone_fixture.memory == 9
    assert class_smartphone_fixture.color == "black"


def test_new_product(three_smartphones: list[Smartphone]) -> None:
    cur_quantity = three_smartphones[0].quantity
    new_quantity = 1
    name = three_smartphones[0].name
    new_product = Smartphone.new_product(
        {"name": name, "quantity": new_quantity}, existing_products=three_smartphones
    )
    assert (new_product == three_smartphones[0]) and (
        new_product.quantity == cur_quantity + new_quantity
    )


def test_new_product2(three_smartphones: list[Smartphone]) -> None:
    new_product = Smartphone.new_product("blahblah")
    assert new_product.name == "noname"


def test_new_product3(three_smartphones: list[Smartphone]) -> None:
    old_price = three_smartphones[0].price
    name = three_smartphones[0].name
    new_product = Smartphone.new_product(
        {"name": name, "price": old_price * 1.2}, existing_products=three_smartphones
    )
    assert (new_product == three_smartphones[0]) and (
        three_smartphones[0].price == old_price * 1.2
    )


def test_new_price(three_smartphones: list[Smartphone]) -> None:
    old_price = three_smartphones[0].price
    three_smartphones[0].price *= 10
    assert three_smartphones[0].price == old_price * 10


# def test_new_product4(three_smartphones: list[Smartphone]) -> None:
#     cur_quantity = three_smartphones[0].quantity
#     new_quantity = 100
#     new_price = 999999.9
#     new_name = three_smartphones[0].name
#     new_product = Smartphone.new_product(
#         {"name": new_name, "quantity": new_quantity, "price": new_price},
#         existing_products=three_smartphones,
#     )
#     assert (new_product == three_smartphones[0]) and (
#         new_product.quantity == cur_quantity + new_quantity
#     )


def test_lower_price(three_smartphones: list[Smartphone]) -> None:
    def mock_input(prompt: str) -> str:
        return "y"

    src.classes.input = mock_input
    old_price = three_smartphones[0].price
    new_price = old_price * 0.8
    three_smartphones[0].price = new_price
    assert three_smartphones[0].price == new_price


def test_negative_price(three_smartphones: list[Smartphone]) -> None:
    output = []
    src.classes.print = lambda s: output.append(s)
    old_price = three_smartphones[0].price
    three_smartphones[0].price = -three_smartphones[0].price
    assert (three_smartphones[0].price == old_price) and (
        output[-1] == "Цена не должна быть нулевая или отрицательная"
    )


def test_print_smartphone(three_smartphones: list[Smartphone]) -> None:
    test_str = str(three_smartphones[0])
    expected_str = (
        f"{three_smartphones[0].name}, {three_smartphones[0].price} руб. "
        + f"Остаток: {three_smartphones[0].quantity} шт."
    )
    assert test_str == expected_str


def test_add(three_smartphones: list[Smartphone]) -> None:
    expected = (
        three_smartphones[0].quantity * three_smartphones[0].price
        + three_smartphones[1].quantity * three_smartphones[1].price
    )
    assert (three_smartphones[0] + three_smartphones[1]) == expected


def test_add_smartphone_to_grass(
    three_smartphones: list[Smartphone], grass_fixture: list[LawnGrass]
) -> None:
    with pytest.raises(TypeError):
        three_smartphones[0] + grass_fixture[0]
