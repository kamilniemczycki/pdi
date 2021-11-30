from src.map import Map

def get_function(argv):
	if len(argv) == 1:
		exit("\nINSTRUKCJA:\n - py main.py search NAZWA_ULICY -- szukaj ulic wg. nazwy\n - py main.py top -- wyświetl najpopularniejsze ulice w każdym województwie")
	return argv[1]

def get_searched_phrase(argv):
	if len(argv) == 2:
		exit("\nWpisz nazwę ulicy, np. py main.py search Legnicka")
	return argv[2]

def get_mapbox(argv):
	if len(argv) == 4:
		return Map(argv[3])

	return None