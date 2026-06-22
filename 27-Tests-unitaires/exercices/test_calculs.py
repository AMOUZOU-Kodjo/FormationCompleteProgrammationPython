"""
Exercice 27.1 : Tests unitaires avec pytest
Écris et exécute des tests pour les fonctions suivantes.
Crée les tests avec pytest.
"""

# Fonctions à tester
def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

def traiter_notes(notes):
    if not notes:
        return {"moyenne": 0, "min": 0, "max": 0}
    return {
        "moyenne": sum(notes) / len(notes),
        "min": min(notes),
        "max": max(notes),
    }

def valider_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# À compléter — écris les tests avec pytest
"""
Tests à créer :
1. test_division_normale
2. test_division_par_zero
3. test_division_nombres_negatifs
4. test_traiter_notes_vide
5. test_traiter_notes_normal
6. test_valider_email_valide
7. test_valider_email_invalide
"""
