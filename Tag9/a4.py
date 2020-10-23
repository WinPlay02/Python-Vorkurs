class Knoten:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.l = left
		self.r = right
	
	def output(self, depth=0):
		tabs = '\t' * depth
		return f"{self.value}\n{tabs}L {self.l.output(depth + 1) if self.l != None else 'None'}\n{tabs}R {self.r.output(depth + 1) if self.r != None else 'None'}"

	def __str__(self):
		#return f"{self.value}\n\tL {self.l}\n\tR {self.r}"
		return self.output(depth=1)

class Baum:
	def __init__(self, root_value, left: Knoten, right: Knoten):
		self.root = Knoten(root_value)
		self.root.l = left
		self.root.r = right
	
	def __str__(self):
		return f"Baum {self.root}"

def tiefensuche(knoten: Knoten):
	print(knoten.output())

def main():
	baum = Baum(15, Knoten(5, Knoten(3), Knoten(12, Knoten(10, Knoten(6, right=Knoten(7))), Knoten(13))), Knoten(16, right=Knoten(20, Knoten(18), Knoten(23))))
	#print(baum)
	tiefensuche(baum.root)