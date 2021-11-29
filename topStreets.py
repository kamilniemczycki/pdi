from src.repositories import Cities, Streets

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

voivodeships = []

class Voivodeship(object):

	def __init__(self, id, name):
		self.id = id
		self.name = name

with open("data/Voivodeships.csv", encoding="utf-8") as fp:
	lines = fp.readlines()
	for line in lines:
		Voivodeship.id = line.split(";")[0]
		Voivodeship.name = line.split(";")[1]
		voivodeships.append(Voivodeship(Voivodeship.id, Voivodeship.name.replace("\n","")))

for voivodeship in voivodeships:
	print(voivodeship.id + " " + voivodeship.name)
	
	
	
	
