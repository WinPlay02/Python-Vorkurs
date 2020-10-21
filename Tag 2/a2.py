#Aufgabe 2 Zettel 01

def gerade(x):
	if x == 0:
		print("Zahl ist gerade")
	elif x == -1:
		print("Zahl ist ungerade")
	return gerade(x-2)

gerade(int(input("Geben Sie eine Zahl ein: ")))