import src.classes
from src.classes import LawnGrass

"""
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

"""


def test_class_init(class_lawngrass_fixture: LawnGrass) -> None:
    assert class_lawngrass_fixture.name == "test_lawngrass"
    assert class_lawngrass_fixture.description == "test_description"
    assert class_lawngrass_fixture.price == 10.5
    assert class_lawngrass_fixture.quantity == 10
    assert class_lawngrass_fixture.color == "black"
    assert class_lawngrass_fixture.country == "Россия"
    assert class_lawngrass_fixture.germination_period == "1 год"


def test_new_product(grass_fixture: list[LawnGrass]) -> None:
    cur_quantity = grass_fixture[0].quantity
    new_quantity = 1
    name = grass_fixture[0].name
    new_product = LawnGrass.new_product(
        {"name": name, "quantity": new_quantity}, existing_products=grass_fixture
    )
    assert (new_product == grass_fixture[0]) and (
        new_product.quantity == cur_quantity + new_quantity
    )


def test_new_product3(grass_fixture: list[LawnGrass]) -> None:
    old_price = grass_fixture[0].price
    name = grass_fixture[0].name
    new_product = LawnGrass.new_product(
        {"name": name, "price": old_price * 1.2}, existing_products=grass_fixture
    )
    assert (new_product == grass_fixture[0]) and (
        grass_fixture[0].price == old_price * 1.2
    )


def test_new_price(grass_fixture: list[LawnGrass]) -> None:
    old_price = grass_fixture[0].price
    grass_fixture[0].price *= 10
    assert grass_fixture[0].price == old_price * 10


# def test_new_product4(grass_fixture: list[LawnGrass]) -> None:
#     cur_quantity = grass_fixture[0].quantity
#     new_quantity = 100
#     new_price = 999999.9
#     new_name = grass_fixture[0].name
#     new_product = lawngrass.new_product(
#         {"name": new_name, "quantity": new_quantity, "price": new_price},
#         existing_products=grass_fixture,
#     )
#     assert (new_product == grass_fixture[0]) and (
#         new_product.quantity == cur_quantity + new_quantity
#     )


def test_lower_price(grass_fixture: list[LawnGrass]) -> None:
    def mock_input(prompt: str) -> str:
        return "y"

    src.classes.input = mock_input
    old_price = grass_fixture[0].price
    new_price = old_price * 0.8
    grass_fixture[0].price = new_price
    assert grass_fixture[0].price == new_price


def test_negative_price(grass_fixture: list[LawnGrass]) -> None:
    output = []
    src.classes.print = lambda s: output.append(s)
    old_price = grass_fixture[0].price
    grass_fixture[0].price = -grass_fixture[0].price
    assert (grass_fixture[0].price == old_price) and (
        output[-1] == "Цена не должна быть нулевая или отрицательная"
    )


def test_print_lawngrass(grass_fixture: list[LawnGrass]) -> None:
    test_str = str(grass_fixture[0])
    expected_str = (
        f"{grass_fixture[0].name}, {grass_fixture[0].price} руб. "
        + f"Остаток: {grass_fixture[0].quantity} шт."
    )
    assert test_str == expected_str


def test_add(grass_fixture: list[LawnGrass]) -> None:
    expected = (
        grass_fixture[0].quantity * grass_fixture[0].price
        + grass_fixture[1].quantity * grass_fixture[1].price
    )
    assert (grass_fixture[0] + grass_fixture[1]) == expected
