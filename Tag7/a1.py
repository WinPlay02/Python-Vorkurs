from typing import Dict, Tuple, List

#a.i
def flaecheninhalt(breite: float , laenge: float) -> float:
    return breite * laenge

#a.ii
def zeichenzaehlen(text: str) -> Dict[str, int]:
    return {character: text.count(character) for character in text}

#a.iii
def fancy_function(namen_und_matrikelnummern: List[Tuple[str, int]], semester: int, bestanden: bool = False) -> None:
    for eintrag in namen_und_matrikelnummern:
        print (f'Student {eintrag[0]} ({eintrag[1]})')
        print (f', im {semester}. Semester, hat')
        print (f'{"nicht " if not bestanden else ""}bestanden.')

#b)
"""
~/Vorkurs$ mypy main.py
Success: no issues found in 1 source file
~/Vorkurs$ mypy --strict main.py
Tag7/a1.py:12: error: Function is missing a return type annotation
Found 1 error in 1 file (checked 1 source file)
~/Vorkurs$ mypy --strict main.py
main.py:5: error: "fancy_function" does not return a value
Found 1 error in 1 file (checked 1 source file)
~/Vorkurs$ mypy --strict main.py
main.py:5: error: unexpected EOF while parsing
Found 1 error in 1 file (checked 1 source file)
~/Vorkurs$ mypy --strict main.py
Success: no issues found in 1 source file
"""