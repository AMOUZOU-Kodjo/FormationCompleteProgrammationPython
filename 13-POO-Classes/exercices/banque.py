"""
Exercice 13.1 : Système bancaire
Crée les classes suivantes :

CompteBancaire :
- Attributs : titulaire, solde, numero
- Méthodes : deposer(montant), retirer(montant), afficher_solde()
- Propriété : solde (vérifie que le solde ne devient pas négatif)

Banque :
- Attributs : nom, comptes (liste de CompteBancaire)
- Méthodes : ajouter_compte(compte), total_depots(), compte_par_numero(numero)
"""

# À compléter
class CompteBancaire:
    def __init__(self, titulaire, solde=0, numero=None):
        pass

    def deposer(self, montant):
        pass

    def retirer(self, montant):
        pass

    def afficher_solde(self):
        pass


class Banque:
    def __init__(self, nom):
        pass

    def ajouter_compte(self, compte):
        pass

    def total_depots(self):
        pass

    def compte_par_numero(self, numero):
        pass


# Tests
if __name__ == "__main__":
    banque = Banque("Ma Banque")
    c1 = CompteBancaire("Alice", 1000, "FR001")
    c2 = CompteBancaire("Bob", 500, "FR002")

    banque.ajouter_compte(c1)
    banque.ajouter_compte(c2)

    c1.deposer(250)
    c1.retirer(100)
    c1.afficher_solde()

    print(f"Total dépôts : {banque.total_depots()} €")
