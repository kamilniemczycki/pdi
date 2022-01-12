import collections
import time
import math
import multiprocessing
from multiprocessing import Process

from src.repositories import Cities, Streets


class SearchProcess(Process):

    def __init__(self, cities, streets, queue):
        Process.__init__(self)
        self.cities = cities
        self.streets = streets
        self.queue = queue

    def run(self):
        results = {}
        for city in self.cities:
            result = run_search(city, self.streets)
            if result > 0:
                results[city] = run_search(city, self.streets)
        self.queue.put(results)


class SearchStreet:

    def __init__(self, city, streets):
        self.city = city
        self.streets = streets
        self.result_value = 0

    def run(self):
        filtered_streets = list(filter(lambda street: self.__check(street, self.city), self.streets))
        streets_sum = sum([self.streets[street] for street in filtered_streets if street in self.streets])
        if streets_sum > 0:
            self.result_value = streets_sum
        return self.result_value

    def __check(self, street, city_name):
        search = self.__clear_city_to_search(city_name)
        if len(search) == 1 and \
                search[0].lower().startswith(street.lower()):
            return True
        elif len(search) == 2 and \
                search[0].lower().startswith(street.lower()) and \
                search[1].lower().startswith(street.lower()):
            return True
        elif len(search) == 3 and \
            search[0].lower().startswith(street.lower()) and \
            search[1].lower().startswith(street.lower()) and \
            search[2].lower().startswith(street.lower()):
            return True

        return False

    def __clear_city_to_search(self, city_name):
        to_remove = ["owa", "owo", "ice", "a"]
        string = city_name.replace("-", " ", 2)
        string_split = string.split(" ")

        modified_str = ""
        for string in string_split:
            suffix = [suff for suff in to_remove if string.endswith(suff)]
            if len(suffix) > 0:
                modified_str += string.removesuffix(suffix[0]) + " "
            else:
                modified_str += string + " "

        if len(modified_str) > 0:
            return modified_str.removesuffix(" ").split(" ")
        elif len(modified_str) == 0 and isinstance(string_split, list):
            return string_split
        return []


def run_search(city, streets):
    return SearchStreet(city, streets).run()


if __name__ == '__main__':
    print("Launched")
    tmp_cities = []
    cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
    
    print("#---------#")
    cities_list = list(
        set(sorted([city.name for city in cities.all()]))
    )
    print("%d cities found" % len(cities_list))

    streets = collections.Counter([
        street.proper_name
        for street in Streets("data/ULIC_Adresowy_2021-10-09.csv").all()
        if len(street.proper_name.replace("-", " ", 2).split(" ")) < 3
    ])
    print("%d streets found" % len(streets))
    print("#---------#\n")

    queue = multiprocessing.Queue()

    results = {}

    interval = 50
    max_processes = 20
    iterations = math.ceil(len(cities_list) / interval / max_processes)
    print("#---------#\nInterval: %d\nMax process: %d\n#---------#\n" % (interval, max_processes))

    for position in range(iterations):
        start_time = time.time()
        processes = []
        position_start = position * interval * max_processes
        for i in range(max_processes):
            cities_to_search = (interval * i) + position_start
            cities_search_list = cities_list[cities_to_search:cities_to_search + interval]
            processes.append(SearchProcess(cities_search_list, streets, queue))

        for process in processes:
            process.start()

        for process in processes:
            results.update(queue.get())
        
        stop_time = time.time()
        calc_time = (stop_time-start_time)*(iterations-position-1)
        print("\nAnalyzed: %d cities" % (interval * max_processes + position_start))
        print("Estimated time to end: %d min and %d sec" % (calc_time/60, calc_time%60))

        for process in processes:
            process.join(timeout=1.0)

    print("\nResults:")
    [
        print("%s: %d" % (city[0], city[1]))
        for city in sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )[:50]
    ]
