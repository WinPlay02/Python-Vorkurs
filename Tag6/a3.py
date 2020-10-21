import configparser
import datetime
import time

# dict 
hours = ["Null", "Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs", "Sieben", "Acht", "Neun", "Zehn", "Elf", "Zwölf"]

zeit = {
	1: "ein",
	2: "zwei",
	3: "drei",
	4: "vier",
	5: "fünf",
	6: "sechs",
	7: "sieben",
	8: "acht",
	9: "neun",
	10: "zehn",
	11: "elf",
	12: "zwölf",
	20: "zwanzig",
	30: "dreißig",
	40: "vierzig",
	50: "fünfzig"
}

def uhrzeit():
	config = configparser.ConfigParser()
	conf = config.read('time_conf.ini')
	wait_interval = int(config['interval']['length'])

	now = datetime.datetime.now()
	print(f" {hours[now.hour % 12]}")