from src.repositories import Streets, Voivodeships


class TopStreetsPerVoivodeship:

    def __init__(self, streets=None, voivodeships=None):
        self.streets = streets or Streets("data/ULIC_Adresowy_2021-10-09.csv")
        self.voivodeships = voivodeships or Voivodeships("data/Voivodeships.csv")

    def print(self):
        self.__print(
            self.__count_streets_per_voivodeship(),
            self.voivodeships
        )

    def __count_streets_per_voivodeship(self):
        street_arr = {}
        for street in self.streets.all():
            if street.voivodeship_id not in street_arr.keys():
                street_arr[street.voivodeship_id] = {}

            proper_name = street.proper_name
            if proper_name not in street_arr[street.voivodeship_id].keys():
                street_arr[street.voivodeship_id][proper_name] = 0
            street_arr[street.voivodeship_id][proper_name] += 1
        return street_arr

    @staticmethod
    def __print(street_arr, voivodeships):
        for arr_element in street_arr:
            print("#---------------------#\n"
                  + "# "
                  + next(filter(lambda obj: obj.id == arr_element, voivodeships.all())).name
                  + "\n#---------------------#")
            [
                print(key, value)
                for (key, value) in sorted(
                    street_arr[arr_element].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:1]
            ]
            print()
