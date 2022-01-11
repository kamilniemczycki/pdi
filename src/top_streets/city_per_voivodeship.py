import collections

from src.repositories import Cities, Voivodeships


class TopCitiesPerVoivodeship:

    def __init__(self, cities=None, voivodeships=None):
        self.cities = cities or Cities("data/SIMC_Urzedowy_2021-10-09.csv")
        self.voivodeships = voivodeships or Voivodeships("data/Voivodeships.csv")

    def print(self):
        self.__cities_per_voivodeship()

    def __popular_in_voivodeship(self, voivodeship_id):
        city_arr = []
        for city in self.cities.all():
            if city.voivodeship_id == voivodeship_id:
                city_arr.append(city.name)
        return collections.Counter(city_arr)

    def __cities_per_voivodeship(self):
        for voivodeship in self.voivodeships.all():
            [city_name, city_count] = self.__popular_in_voivodeship(voivodeship.id).most_common(1)[0]
            print("#---------------------#\n" +
                  "# " + voivodeship.name +
                  "\n#---------------------#")
            print("%s: %d" % (city_name, city_count))
            print()
