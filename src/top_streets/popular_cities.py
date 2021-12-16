from src.top_streets.in_country import TopStreetsInCountry
from src.repositories import Cities


class PopularCities:

    def __init__(self, cities=None):
        self.cities = cities or Cities("data/SIMC_Urzedowy_2021-10-09.csv")
        self.cities_list = []
        self.top = TopStreetsInCountry()

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
        top_streets = self.top.all()

        print("All data has been loaded and the search is started")

        result = {}
        for city_name in cities:
            streets = [street[0] for street in top_streets if self.check(street[0], city_name, cities)]
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
        cities = self.cities_list
        if len(cities) > 0:
            return cities

        for city in self.cities.all():
            cities.append(city.name)
        return cities

    @staticmethod
    def __clear_to_search(string):
        string = string.replace("-", " ", 2)
        string_split = string.split(" ")

        for to_replace in ["ów", "owa", "owo", "ice", "a"]:
            if len(string_split) == 1:
                string_split = [string_split[0].removesuffix(to_replace)]
            elif len(string_split) == 2:
                string_split = [
                    string_split[0].removesuffix(to_replace),
                    string_split[1].removesuffix(to_replace)
                ]
        return string_split
