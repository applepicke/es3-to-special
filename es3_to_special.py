import sys
from random import randint

headers = (
	('class', ''),
	('arm', 'END'),
	('ath', 'AGL'),
	('axe', 'STR'),
	('blk', 'END'),
	('blu', 'STR'),
	('hva', 'END'),
	('lbl', 'STR'),
	('mda', 'END'),
	('spr', 'STR'),
	('dum1', ''),
	('alc', 'INT'),
	('alt', 'CHA'),
	('con', 'INT'),
	('des', 'INT'),
	('enc', 'INT'),
	('ill', 'PER'),
	('mys', 'PER'),
	('res', 'INT'),
	('una', 'AGL'),
	('dum2', ''),
	('acr', 'AGL'),
	('h2h', 'AGL'),
	('lta', 'AGL'),
	('mar', 'PER'),
	('mer', 'CHA'),
	('sec', 'AGL'),
	('sbl', 'AGL'),
	('snk', 'PER'),
	('spe', 'CHA'),
	('att1', 'attr1'),
	('att2', 'attr2'),
)

class_data = [
	["Acrobat", "", "M", "", "", "", "", "", "", "m", "", "", "m", "", "", "", "", "", "", "M", "", "M", "m", "m", "M", "", "", "", "M", "m", "AGL", "END"],
	["Agent", "", "", "", "m", "", "", "", "", "", "", "", "", "m", "", "", "m", "", "", "m", "", "M", "", "M", "", "m", "", "M", "M", "M", "AGL", "CHA"],
  ["Archer", "", "M", "", "M", "", "", "M", "m", "m", "", "", "", "", "", "", "", "", "m", "m", "", "", "", "M", "M", "", "", "", "m", "", "AGL", "PER"],
  ["Assassin", "", "m", "", "m", "", "", "m", "", "", "", "m", "", "", "", "", "", "", "", "", "", "M", "", "M", "M", "", "m", "M", "M", "", "INT", "AGL"],
  ["Barbarian", "m", "M", "M", "M", "M", "", "", "M", "", "", "", "", "", "", "", "", "", "", "m", "", "m", "", "m", "m", "", "", "", "", "", "AGL", "STR"],
  ["Bard", "", "", "", "M", "", "", "M", "m", "", "", "M", "", "", "", "m", "m", "", "", "", "", "M", "", "", "", "m", "m", "", "", "M", "INT", "CHA"],
  ["Battlemage", "", "", "M", "", "", "M", "m", "", "", "", "m", "M", "M", "M", "m", "", "m", "", "", "", "", "", "", "m", "", "", "", "", "", "INT", "STR"],
  ["Crusader", "m", "", "", "M", "M", "M", "M", "m", "", "", "m", "", "", "M", "", "", "", "m", "", "", "", "m", "", "", "", "", "", "", "", "AGL", "STR"],
  ["Healer", "", "", "", "", "m", "", "", "", "", "", "m", "M", "", "", "", "m", "M", "M", "m", "", "", "M", "m", "", "", "", "", "", "M", "CHA", "INT"],
  ["Knight", "m", "", "M", "M", "", "M", "M", "m", "", "", "", "", "", "", "m", "", "", "m", "", "", "", "", "", "", "m", "", "", "", "M", "CHA", "STR"],
  ["Mage", "", "", "", "", "", "", "", "", "", "", "m", "M", "m", "M", "m", "M", "M", "M", "m", "", "", "", "", "", "", "", "m", "", "", "INT", "PER"],
  ["Monk", "", "M", "", "m", "m", "", "", "", "", "", "", "", "", "", "", "", "", "m", "M", "", "M", "M", "m", "m", "", "", "", "M", "", "AGL", "PER"],
  ["Nightblade", "", "", "", "", "", "", "", "", "", "", "", "M", "", "m", "", "M", "M", "", "m", "", "", "", "m", "m", "", "m", "M", "M", "", "AGL", "INT"],
  ["Pilgrim", "", "", "", "m", "", "", "", "M", "", "", "m", "", "", "", "", "m", "", "M", "", "", "", "m", "", "M", "M", "", "m", "", "M", "END", "CHA"],
  ["Rogue", "", "m", "M", "m", "", "", "m", "m", "", "", "", "", "", "", "", "", "", "", "", "", "", "M", "M", "", "M", "", "M", "", "m", "PER", "AGL"],
  ["Scout", "", "M", "", "M", "", "", "M", "M", "", "", "m", "m", "", "", "", "", "", "", "m", "", "", "", "m", "m", "", "", "", "M", "", "END", "AGL"],
  ["Sorcerer", "", "", "", "", "", "m", "", "m", "", "", "", "M", "M", "M", "M", "m", "M", "", "", "", "", "", "", "m", "", "", "m", "", "", "PER", "INT"],
  ["Spellsword", "", "", "m", "M", "m", "", "M", "m", "", "", "m", "M", "", "M", "m", "", "", "M", "", "", "", "", "", "", "", "", "", "", "", "END", "INT"],
  ["Thief", "", "m", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "M", "m", "M", "m", "m", "M", "M", "M", "m", "AGL", "PER"],
  ["Warrior", "m", "M", "m", "M", "m", "M", "M", "M", "m", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "m", "", "", "", "", "", "END", "STR"],
  ["Witchhunter", "", "", "", "m", "m", "", "", "", "", "", "M", "", "M", "", "M", "", "m", "", "m", "", "", "", "M", "M", "", "", "", "m", "", "AGL", "INT"],
]

point_templ = {
	'STR': 0,
	'PER': 0,
	'END': 0,
	'CHA': 0,
	'INT': 0,
	'AGL': 0,
	'LUK': 0,
}

def gen_point_values(_class):
	percs = point_templ.copy()
	percs['LUK'] = 4

	def inc(stat, val):
		inc = 0

		if val == 'm':
			inc = 1
		elif val == 'M':
			inc = 3
		elif val in percs.keys():
			percs[val] += 6

		if stat in percs.keys():
			percs[stat] += inc

	for count, (key, val) in enumerate(headers):
		inc(val, _class[count])

	return percs

def get_point(percs, total):
	count = 0

	for key, val in percs.iteritems():
		rand = randint(1, total)

		if rand >= count and rand <= (count + val):
			return key

		count += val

	return 'LUK'

def gen_points(percs):
	total_count = sum(percs.values())
	points = point_templ.copy()

	count = 0
	while count < 14:
		point = get_point(percs, total_count)

		if points[point] > 8:
			continue

		points[point] += 1
		count += 1

	for point in points.keys():
		points[point] += 1

	return points

def gen_for_class(_class):
	for data in class_data:

		if data[0].lower() != _class.lower():
			continue

		point_values = gen_point_values(data)
		points = gen_points(point_values)

		points['name'] = data[0]
		points['classname'] = data[0].lower()

		return points

PROMPT = """
Available Commands:

<classname>     Generate S.P.E.C.I.A.L points for the specified class
list            Show available class names
exit (q)        Quit the program
"""

CLASS_TEMPL = """
%(name)s
=================
STRENGTH:      %(STR)s
PERCEPTION:    %(PER)s
ENDURANCE:     %(END)s
CHARISMA:      %(CHA)s
INTELLIGENCE:  %(INT)s
AGILITY:       %(AGL)s
LUCK:          %(LUK)s
"""

command = ''
if __name__ == '__main__':
	print "Welcome to the Elder Scrolls III Class  ---->  S.P.E.C.I.A.L translator."

	while True:
		print PROMPT
		command = raw_input("$> ").lower()


		if command in ['exit', 'q']:
			sys.exit(0)

		if command == 'list':
			print 'Available Classes:'
			print ''
			print "\n".join([d[0] for d in class_data])

		if command in [d[0].lower() for d in class_data]:
			print CLASS_TEMPL % gen_for_class(command)

