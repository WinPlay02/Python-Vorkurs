import random
import copy
import time

class GameOfLife:
    def __init__(self):
        self.spielzeit = 0
        self.init_board(int(input("Wieviele Spalten? ")), 
						int(input("Wieviele Zeilen? ")))
    
    def print_board(self):
        print(f"Generation {self.spielzeit}")
        for x in range(self.sizex):
            str_line = ""
            for y in range(self.sizey):
                if self.feld[x][y] == 1:
                    str_line += "⬜ "
                else:
                    str_line += "⬛ "
            print(str_line)

    def init_board(self, sizex, sizey):
        self.sizex = sizex
        self.sizey = sizey
        self.feld = [[random.randrange(0,2) for column in range(sizey)] 
					for row in range(sizex)]
        self.kopie = copy.deepcopy(self.feld)
        self.print_board()
    
    def get_alive_cell_neighbours(self, x, y):
        alive_neighbours = 0
        for xn in range(-1, 2):
            for yn in range(-1, 2):
                if xn == 0 and yn == 0:
                    continue
                try:
                    if (xn + x) < 0 or (yn + y) < 0:
                        raise IndexError()
                    alive_neighbours += self.kopie[x + xn][y + yn]
                except IndexError:
                    continue
        return alive_neighbours

    def is_cell_alive(self, x, y):
        return self.kopie[x][y] == 1
    
    def is_cell_dead(self, x, y):
        return self.kopie[x][y] == 0
    
    def cell_revive(self, x, y):
        self.feld[x][y] = 1
    
    def cell_kill(self, x, y):
        self.feld[x][y] = 0

    def is_any_cell_alive(self):
        for x in range(self.sizex):
            for y in range(self.sizey):
                if self.feld[x][y] == 1:
                    return True
        return False
    
    def is_same_as_last(self):
        for x in range(self.sizex):
            for y in range(self.sizey):
                if self.feld[x][y] != self.kopie[x][y]:
                    return False
        return True
    
    def is_same_as_last2(self):
        for x in range(self.sizex):
            for y in range(self.sizey):
                if self.feld[x][y] != self.kopie2[x][y]:
                    return False
        if self.spielzeit <= 2:
            return False
        return True
    
    def sim_gen(self):
        self.kopie2 = self.kopie
        self.kopie = copy.deepcopy(self.feld)
        for x in range(self.sizex):
            for y in range(self.sizey):
                n = self.get_alive_cell_neighbours(x, y)
                if self.is_cell_dead(x, y) and n == 3: # Regel 1
                    self.cell_revive(x, y)
                if self.is_cell_alive(x, y) and (n < 2 or n > 3): # Regeln 2, 4
                    self.cell_kill(x, y)

        self.spielzeit += 1
    
    def sim_until(self, generations=50):
        while self.spielzeit <= generations and (self.is_any_cell_alive()):
            self.sim_gen()
            self.print_board()
            if not self.is_any_cell_alive():
                print("Vorzeitiger Exitus")
            if self.is_same_as_last():
                print("Verteilung ist stabil (ändert sich nicht mehr)")
                break
            if self.is_same_as_last2():
                print("Verteilung ist metastabil")
                break
    
#nice one winston!!    Wird Metastabil überhaupt mal erreicht?
# danke                 ja, wird erreicht
#                       ja, kam bei mir vorhin raus
#                       alles klar
# Irgendwie ist unsere neighbours funktion kompakter... D:
# Bei uns ist alles recht kompakt geworden -> Die Bedingungen zum abbrechen sind halt das was es lang gemacht hat :D -> Ja, stimmt, aber die sind auch praktisch :D
#Winston einfach übel gecarried ^^, Maschine der Junge!!! WIr haben wenigstens ein bisschen Gedankenwege mit eingebracht... hust hust :D
#Ich hab zumindest die Generationen mit der Website verglichen ^^           #there we go xD

#alles arbeitsteilung !