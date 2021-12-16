from src.cli import get_mapbox
from src.repositories import Cities, Streets
from sys import argv

mapbox = get_mapbox(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)


def search(searched_street):
    counter = 0
    found_streets = streets.find_by_street_name(searched_street)
    for street in found_streets:
        phrase = str(street.city) + ": " + street.get_full_name()
        print(phrase)
        counter = counter + 1
        if mapbox:
            coordinate = mapbox.add_coordinates_for_phrase(phrase)

    print(str(counter) + " streets were found.")

    if mapbox:
        mapbox.prepare_map(searched_street)
