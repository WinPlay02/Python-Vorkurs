from anytree import Node, RenderTree
from anytree.exporter import DotExporter

def main():
	root = Node(15)
	n5 = Node(5, parent=root)
	n3 = Node(3, parent=n5)
	n12 = Node(12, parent=n5)
	n10 = Node(10, parent=n12)
	n6 = Node(6, parent=n10)
	n7 = Node(7, parent=n6)
	n13 = Node(13, parent=n12)
	n16 = Node(16, parent=root)
	n20 = Node(20, parent=n16)
	n18 = Node(18, parent=n20)
	n23 = Node(23, parent=n20)
	#print(RenderTree(root))
	for pre, fill, node in RenderTree(root):
		print("%s%s" % (pre, node.name))
	# DotExporter(root).to_picture('root.png')
  