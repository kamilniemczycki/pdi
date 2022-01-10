from src.repositories import Streets


class TopStreetsInCountry:

    def __init__(self, streets=None):
        self.streets = streets or Streets("data/ULIC_Adresowy_2021-10-09.csv")

    def print(self):
        self.__print(self.__count_streets_in_country())

    def all(self):
        return self.__sort_of_popular(
            self.__count_streets_in_country()
        )

    def all_as_yield(self):
        for street in self.all():
            yield street

    def get_100_as_yield(self):
        get_top = self.all()[:100]
        for street in get_top:
            yield street

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
