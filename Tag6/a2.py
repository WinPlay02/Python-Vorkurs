import datetime
import argparse

def time_since_birth(birth_date, ausgabe):
	delta = datetime.datetime.now() - birth_date
	if ausgabe == 'Sekunden':
		print(delta.total_seconds())
	elif ausgabe == 'Stunden':
		print(delta.total_seconds() / 3600)
	elif ausgabe == "Tage":
		print(delta.total_seconds() / 86400)
	elif ausgabe == "Wochen":
		print(delta.total_seconds() / 604800)
	else:
		print("Unbekannte Ausgabeeinheit")

def arg_time_since_birth():
	parser = argparse.ArgumentParser()
	parser.add_argument('datum', help='Geburtsdatum')
	parser.add_argument('ausgabe', help='Einheit der Ausgabe')
	args = parser.parse_args()
	
	time_since_birth(datetime.datetime.strptime(args.datum, '%d.%m.%Y'), args.ausgabe)
	