import csv
import weakref


class Bewerber(object):
	"""docstring for Bewerber"""
	_instances = set()

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
		self._instances.add(weakref.ref(self))

	@classmethod
	def getinstances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
			cls._instances -= dead


with open('ltw18_bewerberdaten.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(', '.join(row))
		Bewerber(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])


print(Bewerber.getinstances())
