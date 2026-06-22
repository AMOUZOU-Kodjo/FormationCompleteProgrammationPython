"""
Exercice 19.2 : Utilitaire de dates
Crée des fonctions utilitaires avec datetime :

- afficher_maintenant() → "Il est 14:30 le 15/01/2024"
- compter_jours(date1, date2) → nombre de jours entre deux dates
- est_weekend(date) → True si samedi ou dimanche
- age(date_naissance) → âge en années
- lister_vendredis_13(annee) → liste des vendredis 13 d'une année
"""

from datetime import datetime, date

# À compléter
def afficher_maintenant():
    pass

def compter_jours(date1, date2):
    pass

def est_weekend(date):
    pass

def age(date_naissance):
    pass

def lister_vendredis_13(annee):
    pass


# Tests
if __name__ == "__main__":
    afficher_maintenant()
    print(compter_jours(date(2024, 1, 1), date(2024, 12, 31)))
    print(est_weekend(date(2024, 1, 15)))  # lundi → False
    print(age(date(2000, 6, 15)))
    print(lister_vendredis_13(2024))
