"""
Exercice 25.1 : Outils d'introspection
Crée des fonctions d'introspection :

- analyser_objet(obj) : affiche le type, les attributs, méthodes (publiques vs privées)
- signature_complete(func) : retourne un dict avec nom, params, annotations, défauts
- hierarchie_classe(cls) : affiche l'arbre d'héritage complet
- comparer_objets(obj1, obj2) : affiche les différences d'attributs
"""

import inspect

# À compléter
def analyser_objet(obj):
    pass

def signature_complete(func):
    pass

def hierarchie_classe(cls):
    pass

def comparer_objets(obj1, obj2):
    pass


# Tests
if __name__ == "__main__":
    class Animal:
        def __init__(self, nom):
            self.nom = nom

        def parler(self):
            pass

    class Chien(Animal):
        def __init__(self, nom, race):
            super().__init__(nom)
            self.race = race

        def parler(self):
            return "Woof"

    analyser_objet(Chien("Rex", "Berger"))
    print()
    hierarchie_classe(Chien)
