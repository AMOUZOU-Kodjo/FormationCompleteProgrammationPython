"""
Exercice 14.2 : Système d'employés
Crée :

Employe (base) : nom, salaire_base
  - methode : calculer_salaire() → salaire_base

Developpeur(Employe) : langage, prime
  - calculer_salaire() → salaire_base + prime

Manager(Employe) : equipe (liste d'Employe)
  - calculer_salaire() → salaire_base + 100*len(equipe)
  - ajouter_membre(employe)

Stagiaire(Employe) : duree_mois
  - calculer_salaire() → salaire_base * 0.5

Affiche la masse salariale totale.
"""

# À compléter
class Employe:
    pass

class Developpeur(Employe):
    pass

class Manager(Employe):
    pass

class Stagiaire(Employe):
    pass
