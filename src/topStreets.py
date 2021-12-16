from src.repositories import Cities, Streets, Voivodeships

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)
voivodeships = Voivodeships("data/Voivodeships.csv")


def top_streets():
    print_top_street_per_voivodeship(count_streets())


def count_streets():
    street_arr = {}
    for street in streets.all():
        if street.voivodeship_id not in street_arr.keys():
            street_arr[street.voivodeship_id] = {}

        proper_name = street.proper_name
        if proper_name not in street_arr[street.voivodeship_id].keys():
            street_arr[street.voivodeship_id][proper_name] = 0
        street_arr[street.voivodeship_id][proper_name] += 1
    return street_arr


def print_top_street_per_voivodeship(street_arr):
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
