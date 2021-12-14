from src.cli import get_function, get_searched_phrase
from src.search import search
from src.topStreets import top_streets
from sys import argv

function = get_function(argv)

if function == "search":
    searched_street = get_searched_phrase(argv)
    search(searched_street)
if function == "top":
    top_streets()
