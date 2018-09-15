import csv
import weakref


class Bewerber(object):
	"""docstring for Bewerber"""
	_instances = []

	def __init__(self, wahlkreisschluessel, wahlkreisname, wahlvorschlagstraeger, listenplatz, bewerber_im_stimmkreis, titel, firstname, lastname, year_of_birth):
		super(Bewerber, self).__init__()
		self.wahlkreisschluessel = wahlkreisschluessel
		self.wahlkreisname = wahlkreisname
		self.wahlvorschlagstraeger = wahlvorschlagstraeger
		self.listenplatz = listenplatz
		self.bewerber_im_stimmkreis = bewerber_im_stimmkreis
		self.titel = titel
		self.firstname = firstname
		self.lastname = lastname
		self.year_of_birth = year_of_birth
		self._instances.append(self)

	def __str__(self):
		return('' + str(self.firstname) + str(self.lastname) + ' aus der Partei ' + str(self.wahlvorschlagstraeger))


with open('ltw18_bewerberdaten.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		#print(', '.join(row))
		Bewerber(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])


def list_of_partys():
	list_of_partys = []

	for obj in Bewerber._instances:
		if obj.wahlvorschlagstraeger not in list_of_partys:
			list_of_partys.append(obj.wahlvorschlagstraeger)

	return(list_of_partys)

print(list_of_partys())

