class Converter:
    def __init__(self):
        self.__distance_in_meters = 0

    @property
    def meters(self):
        return round(self.__distance_in_meters, 2)
    @meters.setter
    def meters(self, value):
        self.__distance_in_meters = value

    @property
    def inches(self):
        return round(self.__distance_in_meters * 39.3701, 2)
    @inches.setter
    def inches(self, value):
        self.__distance_in_meters = value / 39.3701

    @property
    def feet(self):
        return round(self.__distance_in_meters * 3.28084, 2)
    @feet.setter
    def feet(self, value):
        self.__distance_in_meters = value / 3.28084