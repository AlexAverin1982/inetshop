import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture()
def class_product_fixture() -> Product:
    return Product(
        name="test_product", description="test_description", price=10.5, quantity=10
    )


@pytest.fixture()
def class_category_fixture() -> Category:
    return Category(name="test_category", description="test_description")


@pytest.fixture()
def three_products() -> list[Product]:
    prod1 = Product(name="prod1", quantity=10, price=100.0)
    prod2 = Product(name="prod2", quantity=10, price=100.0)
    prod3 = Product(name="prod3", quantity=10, price=100.0)
    return [prod1, prod2, prod3]


@pytest.fixture()
def class_smartphone_fixture() -> Smartphone:
    return Smartphone(
        name="test_smartphone",
        description="test_description",
        price=10.5,
        quantity=10,
        efficiency=1000.0,
        model="Iphone999",
        memory=9,
        color="black",
    )


@pytest.fixture()
def three_smartphones() -> list[Smartphone]:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )
    return [smartphone1, smartphone2, smartphone3]


@pytest.fixture()
def grass_fixture() -> list[LawnGrass]:
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    return [grass1, grass2]


@pytest.fixture()
def class_lawngrass_fixture() -> LawnGrass:
    return LawnGrass(
        name="test_lawngrass",
        description="test_description",
        price=10.5,
        quantity=10,
        country="Россия",
        germination_period="1 год",
        color="black",
    )
