import json
import os

from src.classes import Category


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
                    aname=cat_item.get("name", ""),
                    adescription=cat_item.get("description", ""),
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
    par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
    data_filename = os.path.join(par_dir, "data", "products.json")

    data_read = load_from_file(data_filename)

    for cat in data_read:
        print(f"{cat.name} : {cat.description}")
        for prod in cat.products:
            print(f"name: {prod.name}")
            print(f"description: {prod.description}")
            print(f"price: {prod.price}")
            print(f"quantity: {prod.quantity}")
            print("-" * 30)
    print("*" * 50)
