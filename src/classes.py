# from pythonlangutil.overload import Overload, signature
from abc import ABC, abstractmethod
from typing import Any

from typing_extensions import Self


class BaseProduct(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    # @abstractmethod
    # def set_owner(self, owner) -> None:
    #     pass


class MixinParentControl:
    """
    Реализуйте класс-миксин, который будет при создании объекта, то есть при работе метода
    __init__
    , печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект.

    Например:

    Product('Продукт1', 'Описание продукта', 1200, 10)
    Добавьте миксин в цепочку наследования класса
    Product.
    """

    def __init__(self, *args, **kwargs):
        arguments = [str(arg) for arg in args]
        class_name = "Unknown_class"
        if kwargs:
            class_name = kwargs.get("class_name", "Unknown_class")
            if class_name != "Unknown_class":
                del kwargs["class_name"]
            # нудно наводим красоту
            if len(kwargs.keys()):
                for ind, param_name in enumerate(
                    ["name", "description", "price", "quantity"]
                ):
                    if kwargs.get(param_name):
                        if len(arguments) > ind:
                            arguments[ind] = str(kwargs.get(param_name))
                        else:
                            arguments.append(str(kwargs.get(param_name)))

                if (
                    class_name == "Smartphone"
                ):  # опять хардкод, но так хоть код будет постройнее
                    for ind, param_name in enumerate(
                        ["efficiency", "model", "memory", "color"]
                    ):
                        if kwargs.get(param_name):
                            if len(arguments) > ind + 4:
                                arguments[ind + 4] = str(kwargs.get(param_name))
                            else:
                                arguments.append(str(kwargs.get(param_name)))
                elif class_name == "LawnGrass":
                    for ind, param_name in enumerate(
                        ["country", "germination_period", "color"]
                    ):
                        if kwargs.get(param_name):
                            if len(arguments) > ind + 4:
                                arguments[ind + 4] = str(kwargs.get(param_name))
                            else:
                                arguments.append(str(kwargs.get(param_name)))

        param_values = "', '".join(arguments)
        object_representation = f"{class_name}('{param_values}')"
        print(object_representation)


class Product(MixinParentControl, BaseProduct):

    def __init__(self, *args, **kwargs):
        self.name: str = ""
        self.description: str = ""
        self.__price: float = 0.0
        self.quantity: int = 0
        if (
            args
        ):  # очень странный блок, но я не знаю, как еще передать args и kwargs в класс-примесь
            self.name = str(args[0])
            if len(args) > 1:
                self.description = str(args[1])
                if (len(args) > 2) and isinstance(args[2], (float, int)):
                    self.__price = float(args[2])
                    if (len(args) > 3) and isinstance(args[3], int):
                        self.quantity = int(args[3])
        if kwargs:
            self.name = kwargs.get("name", self.name)
            self.description = kwargs.get("description", self.description)
            self.__price = kwargs.get("price", self.__price)
            self.quantity = kwargs.get("quantity", self.quantity)
            kwargs["class_name"] = self.__class__.__name__
        else:
            kwargs = {"class_name": self.__class__.__name__}
        # self.__owner = None
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """ОТладочное представление продукта"""
        values = [str(val) for val in self.__dict__.values()]
        return f"{self.__class__.__name__}({', '.join(values)})"

    def __str__(self) -> str:
        """Представление продукта для пользователя"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Вычисление общей стоимости всех товаров"""
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    # def __iter__(self):
    #     return self

    @classmethod
    def new_product(
        cls, product_data: dict, existing_products: list[Self] | None = None
    ) -> Self | None:
        result = None
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

    # def set_owner(self, owner) -> None:
    #     self.__owner = owner

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


class Smartphone(Product):
    def __init__(self, *args, **kwargs):
        """
        name: str = 'noname'
        description: str = ""
        price: float = 0.0
        quantity: int = 0
        efficiency: float = 0.0
        model: str = ""
        memory: int = 0
        color: str = ""
        """

        self.efficiency: float = 0.0
        self.model: str = ""
        self.memory: int = 0
        self.color: str = ""

        if (
            args
        ):  # снова странный блок, но я все еще не знаю, как еще передать args и kwargs в примесь...
            if (len(args) > 4) and isinstance(args[2], (float, int)):
                self.efficiency = float(args[4])
                if len(args) > 5:
                    self.model = str(args[5])
                    if (len(args) > 6) and isinstance(args[6], int):
                        self.memory = args[6]
                        if len(args) > 7:
                            self.color = str(args[7])
        if kwargs:
            self.efficiency = kwargs.get("efficiency", self.efficiency)
            self.model = kwargs.get("model", self.model)
            self.memory = kwargs.get("memory", self.memory)
            self.color = kwargs.get("color", self.color)
        else:
            kwargs = {"class_name": self.__class__.__name__}
        # self.__owner = None
        super().__init__(*args, **kwargs)


class LawnGrass(Product):
    def __init__(self, *args, **kwargs):
        """
        name: str,
        description: str = "",
        price: float = 0.0,
        quantity: int = 0,
        country: str = "",  # страна-производитель
        germination_period: str = "",  # срок прорастания
        color: str = "",  # цвет
        """
        self.color: str = ""
        self.country: str = ""
        self.germination_period: str = ""
        if (
            args
        ):  # снова странный блок, но я все еще не знаю, как еще передать args и kwargs в примесь...
            if len(args) > 4:
                self.country = str(args[4])
                if len(args) > 5:
                    self.germination_period = str(args[5])
                    if len(args) > 6:
                        self.color = str(args[6])
        if kwargs:
            self.country = kwargs.get("country", self.country)
            self.germination_period = kwargs.get(
                "germination_period", self.germination_period
            )
            self.color = kwargs.get("color", self.color)
        else:
            kwargs = {"class_name": self.__class__.__name__}
        # self.__owner = None
        super().__init__(*args, **kwargs)


class ProductPortion(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> None:
        pass

    @abstractmethod
    def add_product(self, product: Any, count: int = 1) -> None:
        pass


class Category(ProductPortion):
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(
        self, name: str, description: str = "", products: list[Product] | None = None
    ):
        """
        конструктор
        :param name: имя категории
        :param description:  описание категории
        :param products: список уже созданных объектов продукции, включаемых в создаваемую категорию
        """
        super().__init__()
        Category.category_count += 1
        self.name = name
        self.description = description
        # список товаров категории
        self.__products: list[Product] = []
        self.product_names: list[str] = []
        self.__current_prod_index: int = -1  # для итерации по продуктам категории
        if products:
            self.__products = products
            self.product_names = [prod.name for prod in self.__products]
            Category.product_count += len(self.__products)
            # for prod in self.__products:
            #     prod.set_owner(self)

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(self.product_names)}"

    def __del__(self) -> None:
        """
        деструктор
        уменьшает общее число категорий
        :return:
        """
        Category.category_count -= 1

    def products_count(self) -> int:
        """
        общее количество продуктов данной категории
        return:
        """
        count = 0
        for prod in self.__products:
            count += prod.quantity
        return count

    def __repr__(self) -> str:
        return f"{self.name}, количество продуктов: {self.products_count()} шт."

    def __iter__(self) -> Self:
        """Возвращает итератор"""
        # self.__current_prod_index: int = -1       # для итерации по продуктам категории
        return self

    def __next__(self) -> Product:
        """Возвращает следующий продукт категории"""
        if self.__current_prod_index + 1 < len(self.__products):
            self.__current_prod_index += 1
            return self.__products[self.__current_prod_index]
        else:
            self.__current_prod_index = -1
            raise StopIteration

    # @Overload
    # @signature("str")
    # @signature("str, str, float, int")
    # def add_product(
    #         self,
    #         product_name: str,
    #         product_description: str = "",
    #         product_price: float = 0.0,
    #         product_quantity: int = 0,
    # ) -> None:
    #     product = Product(
    #         name=product_name,
    #         description=product_description,
    #         quantity=product_quantity,
    #         price=product_price,
    #     )
    #     Category.product_count += 1
    #
    #     self.__products.append(product)
    #     self.product_names.append(product.name)

    # @add_product.overload
    # @signature("Product")
    def add_product(self, product: Any, count: int = 1) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_names.append(product.name)
            # product.set_owner(self)
            Category.product_count += count  # for whatever reason....
        else:
            raise TypeError

    # @add_product.overload
    # @signature("Smartphone")
    # def add_product(self, product: Smartphone) -> None:
    #     self.__products.append(product)
    #     self.product_names.append(product.name)
    #     product.set_owner(self)
    #     Category.product_count += 1

    def delete_product(self, product_name: str) -> None:
        if product_name in self.product_names:
            ind = self.product_names.index(product_name)
            del self.__products[ind]
            del self.product_names[ind]
            Category.product_count -= 1

    @property
    def products(self) -> str:
        return "\n".join([str(prod) for prod in self.__products])

    def get_product_by_index(self, ind: int) -> Product | None:
        """Служебный метод для полчения продукта по индексу в списке"""
        if ind in range(len(self.__products)):
            return self.__products[ind]
        elif (ind < 0) and (abs(ind) - 1) in range(len(self.__products)):
            return self.__products[ind]
        else:
            return None


class CategoryMeta:
    """Тестирование итерации по объектам агрегата"""

    def __init__(self, category: Category):
        self.category: Category = category

    def get_total_cost(self) -> float:
        """Стоимость всех продуктов"""
        result = 0.0
        for prod in self.category:
            result += prod.quantity * prod.price
        return result


class Order(ProductPortion):
    overall_count: int = 0
    """
    Создать класс «Заказ», в котором будет ссылка на то,
    какой товар был куплен, количество купленного товара, а также итоговая стоимость.
    В заказе может быть указан только один товар.
    """

    def __init__(self, product: Product, count: int):
        super().__init__()
        Order.overall_count += 1
        self.product = product
        self.count = count
        self.total = product.price * count

    def __str__(self) -> str:
        return (
            f"{self.product.name}: {self.product.price} * {self.count} = {self.total}"
        )

    def add_product(self, product: Any, count: int = 1) -> None:
        if isinstance(product, Product):
            self.product = product
            self.count = count
            self.total = product.price * count
        else:
            raise TypeError
