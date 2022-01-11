class City(object):
    def __init__(self, name, voivodeship_id=None):
        self.name = name
        self.voivodeship_id = voivodeship_id

    def __str__(self):
        return self.name


class Street(object):
    def __init__(self, properties):
        self.voivodeship_id = properties.split(";")[0]
        self.prefix = properties.split(";")[6]
        self.additional_name = properties.split(";")[8]
        self.proper_name = properties.split(";")[7]
        self.city_id = properties.split(";")[4]
        self.city = None

    def get_full_name(self):
        name = self.prefix + " " + self.additional_name + " " + self.proper_name
        return " ".join(name.split())

    def set_city(self, city):
        self.city = city


class Voivodeship(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name
