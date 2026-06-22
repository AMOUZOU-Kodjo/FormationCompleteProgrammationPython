"""
Exercice 15.1 : Classe Vecteur mathématique
Implémente la classe Vecteur2D avec :
- __init__(x, y)
- __str__ et __repr__
- __add__, __sub__
- __mul__(scalaire) et __rmul__(scalaire)
- __eq__, __neg__ (-vecteur)
- __abs__ : norme du vecteur
- __getitem__ : accès par index (0→x, 1→y)
- __iter__ : itération sur (x, y)
- méthode : produit_scalaire(other)
- méthode : angle(other) en radians
"""

import math

# À compléter
class Vecteur2D:
    pass

# Tests
if __name__ == "__main__":
    v1 = Vecteur2D(3, 4)
    v2 = Vecteur2D(1, 2)

    print(v1)              # Vecteur2D(3, 4)
    print(v1 + v2)         # Vecteur2D(4, 6)
    print(v1 - v2)         # Vecteur2D(2, 2)
    print(v1 * 3)          # Vecteur2D(9, 12)
    print(3 * v1)          # Vecteur2D(9, 12)
    print(abs(v1))         # 5.0
    print(v1[0])           # 3
    print(v1.produit_scalaire(v2))  # 11
    print(v1 == Vecteur2D(3, 4))    # True
