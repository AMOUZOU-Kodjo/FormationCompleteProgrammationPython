"""
Exercice 21.1 : Pipeline de traitement de données
Crée un pipeline de transformations pour une liste de dictionnaires.

Étapes :
1. filter : garde les personnes majeures (âge >= 18)
2. map : ajoute un champ "categorie" (âge < 25 : "jeune", 25-50 : "adulte", > 50 : "senior")
3. map : formate en "NOM (âge) - catégorie"
4. reduce : concatène en une chaîne avec séparateur ", "
"""

from functools import reduce

personnes = [
    {"nom": "Alice", "age": 17},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 32},
    {"nom": "David", "age": 15},
    {"nom": "Eve", "age": 55},
    {"nom": "Frank", "age": 22},
]

# À compléter — utilise map, filter, reduce avec des lambda
majeures = list(filter(lambda p: p["age"] >= 18, personnes))
# ... continue le pipeline

resultat = ""
print(resultat)
# Attendu : "Bob (25) - adulte, Charlie (32) - adulte, Eve (55) - senior, Frank (22) - jeune"
