#Aufgabe 1 Zettel 01

#Teil a
class Geburtstag:
	def __init__(self):
		self.Tag = int(input("An welchem Tag wurden Sie geboren? Format (TT)"))
		self.Monat = int(input("In welchem Monat wurden Sie geboren? Format (MM)"))
		self.Jahr = int(input("In welchem Jahr wurden Sie geboren? Format (JJJJ)"))
		
	def print(self):	
		print(str(self.Tag)+"."+str(self.Monat)+"."+str(self.Jahr))

#Teil b
	def nice_print(self):
		Monate = ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
		print(str(self.Tag)+"."+Monate[self.Monat-1],str(self.Jahr))


x = Geburtstag()
x.print()
x.nice_print()
