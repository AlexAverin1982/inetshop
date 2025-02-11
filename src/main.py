import json
import os

from src.classes import Category, Product


def load_from_file(filename: str) -> list[Category]:
    categories = []
    if not os.path.exists(filename):
        return []
    if not os.path.isfile(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read()
        data = json.loads(lines)
    if data:
        if isinstance(data, list):
            for cat_item in data:
                new_cat = Category(
                    name=cat_item.get("name", ""),
                    description=cat_item.get("description", ""),
                )
                products = cat_item.get("products", [])
                for prod_item in products:
                    new_cat.add_product(
                        product_name=prod_item.get("name", ""),
                        product_description=prod_item.get("description", ""),
                        product_price=prod_item.get("price", 0.0),
                        product_quantity=prod_item.get("quantity", 0),
                    )
                categories.append(new_cat)
    return categories


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
