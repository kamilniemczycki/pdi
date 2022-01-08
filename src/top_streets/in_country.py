from src.repositories import Streets


class TopStreetsInCountry:

    def __init__(self, streets=None):
        self.streets = streets or Streets("data/ULIC_Adresowy_2021-10-09.csv")

    def print(self):
        self.__print(self.__count_streets_in_country())

    def get_top(self):
        return self.__sort_of_popular(
            self.__count_streets_in_country()
        )

    def __count_streets_in_country(self):
        street_arr = {}
        for street in self.streets.all():
            proper_name = street.proper_name
            if proper_name not in street_arr.keys():
                street_arr[proper_name] = 0
            street_arr[proper_name] += 1
        return street_arr

    @staticmethod
    def __sort_of_popular(streets):
        return sorted(
            streets.items(),
            key=lambda x: x[1],
            reverse=True
        )

    @staticmethod
    def __print(streets):
        sort_of_popular = TopStreetsInCountry.__sort_of_popular(streets)
        [
            print("%s: %4d" % (key, value))
            for (key, value) in sort_of_popular[:100]
        ]
