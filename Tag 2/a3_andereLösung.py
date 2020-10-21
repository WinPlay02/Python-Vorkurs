#Aufgabe 3 Zettel 01

# anderer Ansatz

liste = []

import random

for i in range(20):
	liste.append(random.randrange(0,9999))

for x in range(len(liste) - 1):
	for a in range(len(liste) - x - 1):
		if liste[a+1] < liste[a]:
			liste[a+1], liste[a] = liste[a], liste[a+1]

print(liste)