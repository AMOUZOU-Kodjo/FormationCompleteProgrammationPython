"""
Exercice 26.1 : Implémentation de design patterns
Crée les patterns suivants :

1. Singleton : Configuration (chargée une seule fois)

2. Factory : Fabrique de formes géométriques
   - Cercle, Carre, Triangle
   - Chacune a une méthode aire()

3. Observateur :
   - Stock (sujet) avec prix
   - Investisseur (observateur) notifié quand le prix change

4. Stratégie :
   - Calculateur de taxe avec différentes stratégies
   - TaxeFrance (20%), TaxeUSA (variable par état), TaxeZero
"""

from abc import ABC, abstractmethod

# À compléter

# 1. Singleton
class Configuration:
    pass

# 2. Factory de formes
class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

class FabriqueFormes:
    pass

# 3. Observateur
class Stock:
    pass

class Investisseur:
    pass

# 4. Stratégie de taxe
class StrategieTaxe(ABC):
    @abstractmethod
    def calculer(self, montant):
        pass

class CalculateurTaxe:
    pass


# Tests
if __name__ == "__main__":
    # Factory
    cercle = FabriqueFormes.creer("cercle", 5)
    print(f"Cercle aire: {cercle.aire():.2f}")

    # Observateur
    apple = Stock("Apple", 150)
    inv1 = Investisseur("Alice")
    inv2 = Investisseur("Bob")
    apple.attacher(inv1)
    apple.attacher(inv2)
    apple.prix = 155

    # Stratégie
    calc = CalculateurTaxe(StrategieTaxe("france"))
    print(f"Taxe France: {calc.calculer(100)}€")  # 120€
