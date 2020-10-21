matrix = [[1 if row == 2 or column == 2 else 0 for column in range(0,5)] 
			for row in range(0,5)] 
# [[1 if spalte % 5 == 3 or zeile % 5 == 3 else 0 for spalte in range(1, 6)] for zeile in range(1, 6)]
for row in matrix:
	print(row)