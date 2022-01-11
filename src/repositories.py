from src.places import City, Street, Voivodeship


class Cities(object):
    def __init__(self, file):
        self.file = file
        self.lines = []
        self.__load_lines()

    def all(self):
        for line in self.lines:
            yield City(line.split(";")[6], line.split(";")[0])

    def find_by_id(self, city_id):
        for line in self.lines:
            city = self.__find_exact_city(line, city_id)

            if not city:
                city = self.__find_fallback_city(line, city_id)

            if city:
                return city

        return City("? (" + city_id + ")")

    def __load_lines(self):
        with open(self.file, encoding="utf-8") as fp:
            self.lines = list(
                filter(lambda x: (x != "\n"), fp.readlines()[1:])
            )

    @staticmethod
    def __find_exact_city(line, city_id):
        if city_id + ";" + city_id in line:
            return City(line.split(";")[6])

    @staticmethod
    def __find_fallback_city(line, city_id):
        if city_id in line:
            return City(line.split(";")[6])


class Streets(object):
    def __init__(self, file, cities=None):
        self.file = file
        self.cities = cities

    def all(self):
        for line in self.__load_lines():
            yield Street(line)

    def find_by_street_name(self, street_name):
        for line in self.__load_lines():
            if street_name.lower() in line.lower():
                street = Street(line)
                if self.cities is not None:
                    street.set_city(self.cities.find_by_id(street.city_id))
                yield street

    def find_by_voivodeship_id(self, voivodeship_id):
        for line in self.__load_lines():
            if voivodeship_id in line.lower():
                street = Street(line)
                street.set_city(self.cities.find_by_id(street.city_id))
                yield street

    def __load_lines(self):
        with open(self.file, encoding="utf-8") as file:
            lines = file.readlines()[1:]
            for line in lines:
                if line not in "\n":
                    yield line


class Voivodeships:
    def __init__(self, file):
        self.file = file
        self.voivodeships = []

    def all(self):
        self.__load_to_array()
        return self.voivodeships

    def find_by_id(self, voivodeship_id):
        self.__load_to_array()
        return next((voivodeship for voivodeship in self.voivodeships if voivodeship.id == voivodeship_id), None)

    def __load_to_array(self):
        if not self.voivodeships:
            self.__load_with_file()

    def __load_with_file(self):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                line = line[:-1].split(";")
                self.voivodeships.append(Voivodeship(line[0], line[1]))
