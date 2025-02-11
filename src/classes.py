import copy


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
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(name=product_data.get('name', 'noname'),
                   description=product_data.get('description', ''),
                   price=product_data.get('price', 0),
                   quantity=product_data.get('quantity', 0))


class Category:
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(
            self,
            name: str,
            description: str = "",
            products: list[Product] = None
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

    def __del__(self) -> None:
        Category.category_count -= 1

    def add_product(
            self,
            product_name: str,
            product_description: str = "",
            product_price: float = 0.0,
            product_quantity: int = 0,
    ) -> Product:
        product = Product(
            name=product_name,
            description=product_description,
            quantity=product_quantity,
            price=product_price,
        )
        Category.product_count += 1

        self.__products.append(product)
        self.product_names.append(product.name)
        return product

    def delete_product(self, product_name: str) -> None:
        if product_name in self.product_names:
            ind = self.product_names.index(product_name)
            del self.__products[ind]
            del self.product_names[ind]
            Category.product_count -= 1

    @property
    def products(self):
        return '\n'.join([f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.' for prod in self.__products])

