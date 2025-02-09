class Product:
    def __init__(self, aname: str, adescription: str = '', aprice: float = 0.0, aquantity: int = 0):
        self.name = aname
        self.description = adescription
        self.price = aprice
        self.quantity = aquantity


class Category:
    # количество категорий
    category_count: int = 0

    # количество товаров
    product_count: int = 0

    # список товаров категории
    products: list[Product] = []

    def __init__(self, aname: str, adescription: str = '', aprice: float = 0.0, aquantity: int = 0):
        Category().category_count += 1
        self.name = aname
        self.description = adescription

    def add_product(self, product_name: str, product_description: str = '', aquantity: int = 0) -> Product:
        product = Product(aname=product_name, adescription=product_description, aquantity=aquantity)
        self.product_count += aquantity
        self.products.append(product)
        return product

    """
    """
