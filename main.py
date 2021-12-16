from src.cli import get_function, get_searched_phrase
from src.search import search
from src.top_streets.per_voivodeship import TopStreetsPerVoivodeship
from src.top_streets.in_country import TopStreetsInCountry
from src.top_streets.popular_cities import PopularCities
from sys import argv

function = get_function(argv)

if function == "search":
    searched_street = get_searched_phrase(argv)
    search(searched_street)
if function == "top":
    TopStreetsPerVoivodeship().print()
if function == "top_country":
    TopStreetsInCountry().print()
if function == "popular_cities":
    PopularCities().print()
