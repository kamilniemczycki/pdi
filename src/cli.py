from src.map import Map


def get_function(argv):
    if len(argv) == 1:
        exit(
            "\nINSTRUKCJA:\n" +
            "- py main.py search NAZWA_ULICY -- szukaj ulic wg. nazwy\n" +
            "- py main.py top -- wyświetl najpopularniejsze ulice w każdym województwie\n" +
            "- py main.py top_country -- wyświetl najpopularniejsze ulice w kraju\n" +
            "- py main.py popular_cities -- wyświetl najpopularniejsze ulice w kraju")
    return argv[1]


def get_searched_phrase(argv):
    if len(argv) == 2 and argv[1] == "search":
        exit("\nWpisz nazwę ulicy, np. py main.py search Legnicka")
    return argv[2]


def get_mapbox(argv):
    if len(argv) == 4:
        return Map(argv[3])

    return None
