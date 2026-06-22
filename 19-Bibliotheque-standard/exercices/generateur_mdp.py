"""
Exercice 19.1 : Générateur de mots de passe
Utilise random, string et secrets pour créer un générateur de mots de passe.

Fonctions à créer :
- generer_mdp(longueur=12, min_maj=True, min_chiffres=True, min_speciaux=True)
- generer_pin(longueur=6)
- evaluer_force(mdp) → "faible" / "moyen" / "fort" / "très fort"

Le mot de passe doit contenir au moins :
- 1 majuscule
- 1 minuscule
- 1 chiffre
- 1 caractère spécial
"""

import random
import string
import secrets

# À compléter
def generer_mdp(longueur=12, min_maj=True, min_chiffres=True, min_speciaux=True):
    pass

def generer_pin(longueur=6):
    pass

def evaluer_force(mdp):
    pass


# Tests
if __name__ == "__main__":
    mdp = generer_mdp(16)
    print(f"Mot de passe : {mdp}")
    print(f"Force : {evaluer_force(mdp)}")
    print(f"PIN : {generer_pin(8)}")
