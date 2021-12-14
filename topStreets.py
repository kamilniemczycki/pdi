from src.repositories import Cities, Streets
from collections import Counter

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

voivodeships = []
streetNames = []

class Voivodeship(object):

	def __init__(self, id, name):
		self.id = id
		self.name = name

def topStreets():
	with open("data/Voivodeships.csv", encoding="utf-8") as fp:
		lines = fp.readlines()
		for line in lines:
			Voivodeship.id = line.split(";")[0]
			Voivodeship.name = line.split(";")[1]
			voivodeships.append(Voivodeship(Voivodeship.id, Voivodeship.name.replace("\n","")))

	for voivodeship in voivodeships:
		print("\n" + voivodeship.name + "\n")
	
		found_streets = streets.find_by_voivodeship_id(voivodeship.id)
		for street in found_streets:
			if street.voivodeship_id == voivodeship.id:
				streetNames.append(street.get_full_name())
	
		print(Counter(streetNames).most_common(1))
		streetNames.clear()
