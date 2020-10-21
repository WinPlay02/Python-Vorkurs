alice = ['Bananen', 'Brot', 'Schokolade', 'Rotwein']
bob = ['Bier', 'Bier', 'Chips']
eve = ['Brot', 'Schokolade', 'Chips', 'Bier', 'Wasser']

gesamtliste = alice + bob + eve
liste = {}

for ware in gesamtliste:
  if not ware in liste:
    liste[ware] = 1
  else:
    liste[ware] = liste[ware] +1

#Teil b
for ware in liste:
  print(ware, ":", liste[ware])
