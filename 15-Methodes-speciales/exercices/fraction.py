"""
Exercice 15.2 : Classe Fraction
Crée une classe Fraction avec :
- __init__(numerateur, denominateur)
- __str__ → "3/4"
- __add__, __sub__, __mul__, __truediv__
- __eq__, __lt__, __gt__
- __float__ → conversion en float
- propriété : simplifie() → fraction réduite (3/6 → 1/2)
- propriété : valeur_decimale
"""

import math

# À compléter
class Fraction:
    pass

# Tests
if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    print(f1 + f2)  # 5/6
    print(f1 * f2)  # 1/6
    print(float(f1))  # 0.5
    print(Fraction(4, 6).simplifie())  # 2/3
