from typing import override


class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_be_sold_to(self, person):
        return True

class AgeRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.age_limit = 18

    def can_be_sold_to(self, person):
        return person.age >= self.age_limit

class CountryRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.country = "Arstotzka"

    def can_be_sold_to(self, person):
        return person.country != self.country

class ShoppingList:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)
