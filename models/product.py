"""
Author: Fabio Daros start in 14.02.204
"""

from utils.helper import format_float_coin


class Product:
    counter: int = 1

    def __init__(self, name: str, price: float) -> None:
        self.__code: int = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Code: {self.code} \nName: {self.name} \nPrice: {format_float_coin(self.price)}'
