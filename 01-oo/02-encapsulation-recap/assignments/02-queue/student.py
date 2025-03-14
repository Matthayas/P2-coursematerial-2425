class Queue:
    def __init__(self):
        self.__items = []

    def add(self, person):
        self.__items.append(person)

    def next(self):
        if self.__items.__len__() == 0:
            return None
        person = self.__items[0]
        self.__items.pop(0)
        return person

    def is_empty(self):
        if self.__items.__len__() == 0:
            return True
        return False