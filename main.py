from src.cli import get_function, get_searched_phrase
from src.search import search
from src.top_streets.street_per_voivodeship import TopStreetsPerVoivodeship
from src.top_streets.city_per_voivodeship import TopCitiesPerVoivodeship
from src.top_streets.in_country import TopStreetsInCountry
from src.top_streets.popular_cities import PopularCities
from src.top_streets.duplicated_street import DuplicatedStreet
from sys import argv

function = get_function(argv)

if function == "search":
    searched_street = get_searched_phrase(argv)
    search(searched_street)
if function == "top_street_per_voivodeship":
    TopStreetsPerVoivodeship().print()
if function == "top_city_per_voivodeship":
    TopCitiesPerVoivodeship().print()
if function == "top_street_in_country":
    TopStreetsInCountry().print()
if function == "popular_cities":
    PopularCities().print()
if function == "duplicated_street":
    DuplicatedStreet().print()
