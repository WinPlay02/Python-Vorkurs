#Aufgabe 3 Zettel 01

import random

def sort(liste):
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(liste) -1):
			if liste[i] > liste[i+1]:
				liste[i+1], liste[i] = liste[i], liste[i+1]
				sorted = False
	return liste

Zahlen = []
for i in range(10):
	Zahlen.append(random.randrange(0,99))

print(sort(Zahlen))