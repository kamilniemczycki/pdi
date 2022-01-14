import collections
from src.repositories import Cities, Streets


class PopularCities:

    def __init__(self, cities=None):
        self.cities = cities or Cities("data/SIMC_Urzedowy_2021-10-09.csv")
        self.cities_list = []

    def check(self, street, city_name, arr):
        search = self.__clear_to_search(city_name)
        if len(search) == 1 and \
                search[0].lower().startswith(street.lower()):
            return True
        elif len(search) == 2 and \
                search[0].lower().startswith(street.lower()) and \
                search[1].lower().startswith(street.lower()):
            return True

        return False

    def print(self):
        cities = self.__names_of_cities()
        top_streets = collections.Counter([
            street.proper_name
            for street in Streets("data/ULIC_Adresowy_2021-10-09.csv").all()
            if len(street.proper_name.replace("-", " ", 2).split(" ")) < 3
        ])

        print("All data has been loaded and the search is started")

        result = {}
        for city_name in cities:
            streets = [street for street in top_streets if self.check(street, city_name, cities)]
            if len(streets):
                result[city_name] = len(streets)

            try:
                print("Search %s city - results: %d" % (city_name, result[city_name]))
            except KeyError:
                print("Search %s city - results: 0" % city_name)

        print("Results:")

        [
            print("%s: %d" % (city[0], city[1]))
            for city in sorted(
                result.items(),
                key=lambda x: x[1],
                reverse=True
            )
        ]

    def __names_of_cities(self):
        cities = list(
            set(sorted([city.name for city in self.cities.all()]))
        )
        return cities

    @staticmethod
    def __clear_to_search(city_name):
        to_remove = ["?w", "owa", "owo", "ice", "a"]
        string = city_name.replace("-", " ", 2)
        string_split = string.split(" ")

        modified_str = ""
        for string in string_split:
            suffix = [suff for suff in to_remove if string.endswith(suff)]
            if len(suffix) > 0:
                modified_str += string.removesuffix(suffix[0]) + " "
            else:
                modified_str += string + " "

        if len(modified_str) > 0:
            return modified_str.removesuffix(" ").split(" ")
        elif len(modified_str) == 0 and isinstance(string_split, list):
            return string_split
        return []
