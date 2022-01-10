import collections

from src.repositories import Streets, Cities


class DuplicatedStreet:

    def __init__(self, cities=None, streets=None):
        self.cities = cities or Cities("data/SIMC_Urzedowy_2021-10-09.csv")
        self.streets = streets or Streets("data/ULIC_Adresowy_2021-10-09.csv")

    def print(self):
        self.__search_duplicated_street()

    def __search_duplicated_street(self):
        temporary = []
        for street in self.streets.all():
            temporary.append(street.proper_name + ";" + str(street.city_id))

        street_collection = collections.Counter(temporary)

        for street_city, count in street_collection.most_common(10):
            if count > 1:
                header = True
                for street in self.streets.all():
                    if (street.proper_name + ";" + str(street.city_id)) == street_city:
                        if header:
                            print()
                            print("#################")
                            print(self.cities.find_by_id(street.city_id))
                            print("#################")
                            header = False
                        print(street.get_full_name())


    @staticmethod
    def __sort_of_popular(streets):
        return sorted(
            streets.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @staticmethod
    def __print(streets):
        sort_of_popular = DuplicatedStreet.__sort_of_popular(streets)
        [
            print("%s: %4d" % (key, value))
            for (key, value) in sort_of_popular[:100]
        ]
