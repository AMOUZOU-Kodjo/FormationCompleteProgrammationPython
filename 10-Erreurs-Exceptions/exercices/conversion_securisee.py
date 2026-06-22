"""
Exercice 10.1 : Conversion sécurisée
Écris des fonctions de conversion qui ne lèvent jamais d'exception :
- convertir_en_int(valeur, defaut=None)
- convertir_en_float(valeur, defaut=None)
- diviser_securise(a, b, defaut=None)
- lire_entier(message) : boucle jusqu'à obtenir un entier valide
"""

# À compléter
def convertir_en_int(valeur, defaut=None):
    pass

def convertir_en_float(valeur, defaut=None):
    pass

def diviser_securise(a, b, defaut=None):
    pass

def lire_entier(message):
    pass

# Tests
if __name__ == "__main__":
    print(convertir_en_int("42"))        # 42
    print(convertir_en_int("abc", 0))   # 0
    print(diviser_securise(10, 2))       # 5.0
    print(diviser_securise(10, 0, "N/A"))# N/A
    age = lire_entier("Quel est ton âge ? ")
    print(f"Âge : {age}")
