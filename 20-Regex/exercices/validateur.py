"""
Exercice 20.1 : Validateur de formulaires avec regex
Crée des fonctions de validation avec regex :

- valider_email(email) → bool
- valider_telephone(tel) → bool (format: 0X XX XX XX XX ou +33 X XX XX XX XX)
- valider_code_postal(cp) → bool (5 chiffres)
- valider_date(date) → bool (format JJ/MM/AAAA)
- valider_heure(heure) → bool (format HH:MM)
- extraire_urls(texte) → liste des URLs trouvées
- censurer_email(email) → "a****@example.com"
"""

import re

# À compléter
def valider_email(email):
    pass

def valider_telephone(tel):
    pass

def valider_code_postal(cp):
    pass

def valider_date(date):
    pass

def valider_heure(heure):
    pass

def extraire_urls(texte):
    pass

def censurer_email(email):
    pass


# Tests
if __name__ == "__main__":
    print(valider_email("user@example.com"))    # True
    print(valider_telephone("06 12 34 56 78"))  # True
    print(valider_code_postal("75001"))         # True
    print(extraire_urls("Visitez https://python.org !"))
    print(censurer_email("alice@example.com"))  # a****@example.com
