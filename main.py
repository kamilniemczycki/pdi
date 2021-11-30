from src.cli import get_function, get_searched_phrase
from search import search
from topStreets import topStreets
from sys import argv

function = get_function(argv)

if function == "search":
	searched_street = get_searched_phrase(argv)
	search(searched_street)
if function == "top":
	topStreets()