from typing_extensions import Self
from pythonlangutil.overload import Overload, signature


class Product:

    def __init__(
            self,
            name: str,
            description: str = "",
            price: float = 0.0,
            quantity: int = 0,
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.__owner = None

    @classmethod
    def new_product(
            cls, product_data: dict, existing_products: list[Self] = None
    ) -> Self:
        if isinstance(product_data, dict):
            name = product_data.get("name", "noname")
            description = product_data.get("description", "")
            price = product_data.get("price", 0.0)
            quantity = product_data.get("quantity", 0)
        else:
            name = "noname"
            description = ""
            price = 0.0
            quantity = 0

        if existing_products:
            for existing_product in existing_products:
                if existing_product.name.lower() == name.lower():
                    result = existing_product
                    result.quantity += quantity
                    if price > result.price:
                        result.price = price
                    break
        else:
            result = cls(
                name=name, description=description, price=price, quantity=quantity
            )

        return result

    def set_owner(self, owner) -> None:
        self.__owner = owner

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(
                "Новая цена ниже текущей? Вы уверены, что хотите установить новую цену? (y/n):"
            )
            if confirmation.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price


class Category:
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(
            self, name: str, description: str = "", products: list[Product] = None
    ):
        Category.category_count += 1
        self.name = name
        self.description = description
        # список товаров категории
        self.__products: list[Product] = []
        self.product_names: list[str] = []
        if products:
            self.__products = products
            self.product_names = [prod.name for prod in self.__products]
            Category.product_count += len(self.__products)
            for prod in self.__products:
                prod.set_owner(self)

    def __del__(self) -> None:
        Category.category_count -= 1

    @Overload
    @signature("str")
    @signature("str, str, float, int")
    def add_product(
            self,
            product_name: str,
            product_description: str = "",
            product_price: float = 0.0,
            product_quantity: int = 0,
    ) -> None:
        product = Product(
            name=product_name,
            description=product_description,
            quantity=product_quantity,
            price=product_price,
        )
        Category.product_count += 1

        self.__products.append(product)
        self.product_names.append(product.name)

    @add_product.overload
    @signature("Product")
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        self.product_names.append(product.name)
        product.set_owner(self)
        Category.product_count += 1

    def delete_product(self, product_name: str) -> None:
        if product_name in self.product_names:
            ind = self.product_names.index(product_name)
            del self.__products[ind]
            del self.product_names[ind]
            Category.product_count -= 1

    @property
    def products(self) -> str:
        return "\n".join(
            [
                f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
                for prod in self.__products
            ]
        )

    def get_product_by_index(self, ind: int) -> Product | None:
        if ind in range(len(self.__products)):
            return self.__products[ind]
        elif (ind < 0) and (abs(ind) - 1) in range(len(self.__products)):
            return self.__products[ind]
        else:
            return None
