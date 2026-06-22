"""
Exercice 28.2 : Debugging
Corrige les bugs dans le code ci-dessous en utilisant
- breakpoint() / pdb
- logging
- Les messages d'erreur Python

Objectif : la fonction doit retourner la moyenne des notes
après avoir retiré la note la plus basse et la plus haute.
"""

import logging

logging.basicConfig(level=logging.DEBUG)

def moyenne_elaguee(notes):
    """Calcule la moyenne après avoir retiré min et max."""
    if notes is None or len(notes) == 0:
        return 0
    if len(notes) <= 2:
        return sum(notes) / len(notes)

    notes_triees = notes.sort()  # BUG 1
    notes_sans_extremes = notes_triees[1:-1]  # BUG 2

    moyenne = sum(notes_sans_extremes) // len(notes_sans_extremes)  # BUG 3
    return moyenne


def traiter_eleves(eleves):
    """Traite une liste d'élèves avec leurs notes."""
    resultats = {}
    for eleve in eleves:
        nom = eleve["nom"]
        notes = eleve["notes"]
        resultats[nom] = moyenne_elaguee(notes)
    return resultats  # BUG 4


# Test
eleves = [
    {"nom": "Alice", "notes": [12, 15, 8, 19, 14]},
    {"nom": "Bob", "notes": [10, 10, 10]},
    {"nom": "Charlie", "notes": [5, 20]},
    {"nom": "David", "notes": []},
]

resultats = traiter_eleves(eleves)
print(resultats)
# Attendu : {"Alice": 13.67, "Bob": 10.0, "Charlie": 12.5, "David": 0}
