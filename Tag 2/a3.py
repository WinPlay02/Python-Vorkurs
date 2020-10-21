#Aufgabe 3 Zettel 01

def compare(liste1, liste2):
    if len(liste1) != len(liste2):
        return False
    for i in range(len(liste1)):
        if liste1[i] != liste2[i]:
            return False
    return True

def sort(liste):
    alte = liste.copy()
    neue = []
    while not compare(alte, neue):
        alte = neue.copy()
        for i in range(len(liste) -1):
            if liste[i] > liste[i+1]:
                liste[i+1], liste[i] = liste[i], liste[i+1]
        neue = liste.copy()
    
    print(liste)

Zahlen = []

for i in range(10):
	Zahlen.append(int(input("Geben Sie eine Zahl für Ihre Liste an: ")))
	

sort(Zahlen)