import random

#code = "1234" # random.randrange
#code = str(random.randrange(0,9999)).zfill(4) # random.randrange
#print("Der Code ist: (Geheim)", code)
code = random.sample(range(10), 4)
code2 = (''.join(map(str, code)))
print("Der Code ist: (Geheim)", code2)

spieler = input("Zahlenkombination: ")

v = 0

while code2 != spieler:  #code2 muss zu code umbenannt werden wenn die andere random funktion verwendet werden soll
    while len(spieler) != 4:
        spieler = input("Bitte keine zu langen oder zu kurzen Nummern eintragen:")
	
    v = v + 1
    z = 0
    b = 0

    for i in range(4):
        if code2[i] == spieler[i]: #code
            z = z + 1
        for j in range(4):
            if code2[i] == spieler[j]: #code
                b = b + 1


    print("Richtige Ziffern:",z)
    print("Vorhandene Ziffern:",b)
    spieler = input("Neue Zahlenkombination: ")
print("Richtig! Glückwunsch!!1!!1")
if v == 0:
    print("Das kannst du aber wirklich nicht erraten haben...")
