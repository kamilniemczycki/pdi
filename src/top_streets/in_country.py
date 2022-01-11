import collections

from src.repositories import Streets


class TopStreetsInCountry:

    def __init__(self, streets=None):
        self.streets = streets or Streets("data/ULIC_Adresowy_2021-10-09.csv")

    def print(self):
        self.__print(self.__count_streets_in_country())

    def all(self):
        return self.__count_streets_in_country()

    def all_as_yield(self):
        for street in self.all():
            yield street

    def get_100_as_yield(self):
        get_top = self.all()[:100]
        for street in get_top:
            yield street

    def __count_streets_in_country(self):
        temporary = []
        for street in self.streets.all():
            temporary.append(street.proper_name)
        street_arr = collections.Counter(temporary)
        return street_arr

    @staticmethod
    def __print(streets):
        [
            print("%s: %4d" % (key, value))
            for (key, value) in streets.most_common(100)
        ]
