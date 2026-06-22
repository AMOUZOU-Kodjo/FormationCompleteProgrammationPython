"""
Exercice 27.2 : Tests unitaires pour la classe CompteBancaire
Reprend la classe CompteBancaire du module 13 et écris des tests complets.

Tests à créer :
1. test_creation_compte_solde_initial
2. test_creation_compte_solde_zero
3. test_deposer_montant_positif
4. test_retirer_solde_suffisant
5. test_retirer_solde_insuffisant (doit lever une erreur)
6. test_deposer_montant_negatif (doit lever une erreur)
7. test_historique_transactions
8. test_plusieurs_comptes_independants
"""

import pytest

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde
        self.transactions = []

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Montant doit être positif")
        self._solde += montant
        self.transactions.append(f"Dépôt: +{montant}€")
        return self._solde

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Montant doit être positif")
        if montant > self._solde:
            raise ValueError("Solde insuffisant")
        self._solde -= montant
        self.transactions.append(f"Retrait: -{montant}€")
        return self._solde

# À compléter — écris les tests
