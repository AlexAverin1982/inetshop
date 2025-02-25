import src.classes


def test_mixin_output() -> None:
    # перенаправляем тестовый вывод в консоль для проверки вывода тестовой информации о созданни объекта класса
    output = []
    src.classes.print = lambda s: output.append(s)

    src.classes.Product("bread", "bread_desc", 50.0, 10)
    expected_output = "Product('bread', 'bread_desc', '50.0', '10')"
    assert expected_output == output[-1]

    src.classes.Smartphone(
        "smart", "smart_desc", 1000.0, 100, 999.9, "iphone", 256, "black"
    )
    expected_output = "Smartphone('999.9', 'iphone', '256', 'black', 'smart', 'smart_desc', '1000.0', '100')"
    assert expected_output == output[-1]

    src.classes.LawnGrass(
        "greengrass", "grass_desc", 500.0, 10, "Russia", "1 year", "light_green"
    )
    expected_output = "LawnGrass('light_green', 'Russia', '1 year', 'greengrass', 'grass_desc', '500.0', '10')"
    assert expected_output == output[-1]
