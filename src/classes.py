# mypy: disable-error-code="no-any-return"
# from pythonlangutil.overload import Overload, signature
from abc import ABC, abstractmethod
from typing import Any

from typing_extensions import Self

from src.custom_exceptions import ZeroProductQuantityException


class BaseProduct(ABC):
    def __init__(self):  # type: ignore
        pass

    @abstractmethod
    def __str__(self):  # type: ignore
        pass

    @abstractmethod
    def __add__(self, other):  # type: ignore
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

    def __init__(self):  # type: ignore
        print(repr(self))


class Product(MixinParentControl, BaseProduct):

    def __init__(
        self, name: str, description: str = "", price: float = 0.0, quantity: int = 0
    ):
        if quantity:
            self.name: str = name
            self.description: str = description
            self.__price: float = price
            self.quantity: int = quantity
            super().__init__()
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __repr__(self) -> str:
        """ОТладочное представление продукта"""
        values = [str(val) for val in self.__dict__.values()]
        values = "', '".join(values)  # type: ignore
        return f"{self.__class__.__name__}('{values}')"

    def __str__(self) -> str:
        """Представление продукта для пользователя"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:  # type: ignore
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
    def __init__(
        self,
        name: str,
        description: str = "",
        price: float = 0.0,
        quantity: int = 0,
        efficiency: float = 0.0,
        model: str = "",
        memory: int = 0,
        color: str = "",
    ):
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
        self.efficiency: float = efficiency
        self.model: str = model
        self.memory: int = memory
        self.color: str = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str = "",
        price: float = 0.0,
        quantity: int = 0,
        country: str = "",  # страна-производитель
        germination_period: str = "",  # срок прорастания
        color: str = "",  # цвет
    ):
        """
        name: str,
        description: str = "",
        price: float = 0.0,
        quantity: int = 0,
        country: str = "",  # страна-производитель
        germination_period: str = "",  # срок прорастания
        color: str = "",  # цвет
        """
        self.color: str = color
        self.country: str = country
        self.germination_period: str = germination_period
        super().__init__(name, description, price, quantity)


class ProductPortion(ABC):
    def __init__(self):  # type: ignore
        pass

    @abstractmethod
    def __str__(self) -> None:  # type: ignore
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
            for product in products:
                if product.quantity == 0:
                    raise ZeroProductQuantityException

            self.__products = products
            self.product_names = [prod.name for prod in self.__products]
            Category.product_count += len(self.__products)
            # for prod in self.__products:
            #     prod.set_owner(self)

    def __str__(self) -> str:  # type: ignore
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
            if count * product.quantity == 0:
                raise ZeroProductQuantityException
            self.__products.append(product)
            self.product_names.append(product.name)
            # product.set_owner(self)
            Category.product_count += 1  # for whatever reason....
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
        """
        Описание содержимого категории
        """
        return "\n".join([str(prod) for prod in self.__products])

    def get_product_by_index(self, ind: int) -> Product | None:
        """Служебный метод для полчения продукта по индексу в списке"""
        if ind in range(len(self.__products)):
            return self.__products[ind]
        elif (ind < 0) and (abs(ind) - 1) in range(len(self.__products)):
            return self.__products[ind]
        else:
            return None

    def middle_price(self) -> float:
        """
        Вычисляем средний ценник товаров категории и 0, если товаров в категории нет
        """
        result = 0.0
        for product in self.__products:
            result += product.price
        try:
            result /= len(self.__products)
        except ZeroDivisionError:
            result = 0.0
        return result


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
        if product.quantity * count:
            self.product = product
            self.count = count
            self.total = product.price * count
        else:
            raise ZeroProductQuantityException

    def __str__(self) -> str:  # type: ignore
        """
        Символьное представление объекта
        """
        return (
            f"{self.product.name}: {self.product.price} * {self.count} = {self.total}"
        )

    def add_product(self, product: Any, count: int = 1) -> None:
        """
        Добавляем продкут в заказ
        :param product:
        :param count: количество продукта в заказе
        """
        if isinstance(product, Product):
            if product.quantity * count:
                self.product = product
                self.count = count
                self.total = product.price * count
            else:
                raise ZeroProductQuantityException
        else:
            raise TypeError
