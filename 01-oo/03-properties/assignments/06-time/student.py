class Time:
    def __init__(self, hours, minutes, seconds):
        if 0 <= hours < 24:
            self.__hours = hours
        else:
            raise ValueError("Invalid hours")

        if 0 <= minutes < 60:
            self.__minutes = minutes
        else:
            raise ValueError("Invalid minutes")

        if 0 <= seconds < 60:
            self.__seconds = seconds
        else:
            raise ValueError("Invalid seconds")

    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
        else:
            raise ValueError("Invalid hours")

    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
        else:
            raise ValueError("Invalid minutes")

    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self, value):
        if 0 <= value < 60:
            self.__seconds = value
        else:
            raise ValueError("Invalid seconds")