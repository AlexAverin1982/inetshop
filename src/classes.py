class Product:
    def __init__(
        self,
        aname: str,
        adescription: str = "",
        aprice: float = 0.0,
        aquantity: int = 0,
    ):
        self.name = aname
        self.description = adescription
        self.price = aprice
        self.quantity = aquantity


class Category:
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(
        self,
        aname: str,
        adescription: str = "",
        aprice: float = 0.0,
        aquantity: int = 0,
    ):
        Category.category_count += 1
        self.name = aname
        self.description = adescription
        # список товаров категории
        self.products: list[Product] = []
        self.product_names: list[str] = []

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
            aname=product_name,
            adescription=product_description,
            aquantity=product_quantity,
            aprice=product_price,
        )
        Category.product_count += 1

        self.products.append(product)
        self.product_names.append(product.name)
        return product

    def delete_product(self, product_name: str) -> None:
        if product_name in self.product_names:
            ind = self.product_names.index(product_name)
            del self.products[ind]
            del self.product_names[ind]
            Category.product_count -= 1
