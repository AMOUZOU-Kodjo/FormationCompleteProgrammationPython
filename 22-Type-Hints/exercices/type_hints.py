"""
Exercice 22.1 : Ajouter les type hints
Ajoute les annotations de type complètes à toutes les fonctions et classes.

Exécute ensuite : pip install mypy && mypy type_hints.py
"""

from typing import List, Dict, Tuple, Optional, Union

# À compléter — ajoute les types
def moyenne(notes):
    if not notes:
        return None
    return sum(notes) / len(notes)

def filtrer_majeurs(personnes):
    return [p for p in personnes if p["age"] >= 18]

def zip_avec_defaut(liste1, liste2, defaut=None):
    longueur = max(len(liste1), len(liste2))
    resultat = []
    for i in range(longueur):
        a = liste1[i] if i < len(liste1) else defaut
        b = liste2[i] if i < len(liste2) else defaut
        resultat.append((a, b))
    return resultat

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, autre):
        return ((self.x - autre.x) ** 2 + (self.y - autre.y) ** 2) ** 0.5


# Tests
if __name__ == "__main__":
    print(moyenne([10, 15, 20]))
    print(filtrer_majeurs([{"nom": "A", "age": 20}, {"nom": "B", "age": 15}]))
    print(zip_avec_defaut([1, 2, 3], ["a", "b"]))
