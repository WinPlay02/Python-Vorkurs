x = float(input("X: "))
op = input("Rechenoperation: ")
y = float(input("Y: "))

if op == '+':
    print("Ergebnis: " + str(x) + " + " + str(y) + " = ", x + y)

elif op == '-':
    print("Ergebnis: " + str(x) + " - " + str(y) + " = ", x - y)

elif op =='*':
    print("Ergebnis: " + str(x) + " * " + str(y) + " = ", x * y)

elif op == '/':
    print("Ergebnis: " + str(x) + " / " + str(y) + " = ", x / y)
    
else:
    print("Deine Eingabe der Rechenoperation war ungültig.")