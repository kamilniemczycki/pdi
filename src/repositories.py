from src.places import City, Street, Voivodeship


class Cities(object):
    def __init__(self, file):
        self.file = file

    def find_by_id(self, city_id):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            city = self.__find_exact_city(lines, city_id)

            if not city:
                city = self.__find_fallback_city(lines, city_id)

            if city:
                return city

        return City("? (" + city_id + ")")

    @staticmethod
    def __find_exact_city(lines, city_id):
        for line in lines:
            if city_id + ";" + city_id in line:
                return City(line.split(";")[6])

    @staticmethod
    def __find_fallback_city(lines, city_id):
        for line in lines:
            if city_id in line:
                return City(line.split(";")[6])


class Streets(object):
    def __init__(self, file, cities=None):
        self.file = file
        self.cities = cities

    def file_lines(self):
        with open(self.file, encoding="utf-8") as file:
            lines = file.readlines()[1:]
            for line in lines:
                if line not in "\n":
                    yield line

    def all(self):
        for line in self.file_lines():
            yield Street(line)

    def find_by_street_name(self, street_name):
        for line in self.file_lines():
            if street_name.lower() in line.lower():
                street = Street(line)
                if self.cities is not None:
                    street.set_city(self.cities.find_by_id(street.city_id))
                yield street

    def find_by_voivodeship_id(self, voivodeship_id):
        for line in self.file_lines():
            if voivodeship_id in line.lower():
                street = Street(line)
                street.set_city(self.cities.find_by_id(street.city_id))
                yield street


class Voivodeships:
    def __init__(self, file):
        self.file = file
        self.voivodeships = []

    def all(self):
        if not self.voivodeships:
            self.load_with_file()
        return self.voivodeships

    def load_with_file(self):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                line = line[:-1].split(";")
                self.voivodeships.append(Voivodeship(line[0], line[1]))
