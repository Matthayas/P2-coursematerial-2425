class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount
    @property
    def currency(self):
        return self.__currency

    def __add__(self, other):
        if other.currency == self.currency:
            return self.__amount + other.amount
        else:
            raise RuntimeError