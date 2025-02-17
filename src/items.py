import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(self.name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.quantity * self.price
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла"""
        cls.all.clear()
        if os.path.exists(filename):
            with open(filename, encoding='CP1251') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        name = str(row['name'])
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)
                    else:
                        raise InstantiateCSVError('Файл items.csv поврежден')
        else:
            raise FileNotFoundError('Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(number):
        num = float(number)
        return int(num)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Файл items.csv поврежден'
