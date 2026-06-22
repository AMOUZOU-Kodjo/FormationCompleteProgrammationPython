"""
Exercice 32.1 : CRUD avec SQLAlchemy
Crée un système de gestion de bibliothèque avec SQLAlchemy.

Tables :
- Auteur : id, nom, date_naissance
- Livre : id, titre, annee, auteur_id (FK), disponible (bool)
- Emprunt : id, livre_id (FK), emprunteur, date_emprunt, date_retour

Fonctions CRUD :
- ajouter_auteur(nom, date_naissance)
- ajouter_livre(titre, annee, auteur_id)
- emprunter_livre(livre_id, emprunteur)
- retourner_livre(livre_id)
- lister_livres_disponibles()
- lister_emprunts_retard(jours_max)
"""

from datetime import datetime, date
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

# À compléter
Base = declarative_base()

class Auteur(Base):
    pass

class Livre(Base):
    pass

class Emprunt(Base):
    pass

# Fonctions CRUD
def ajouter_auteur(session, nom, date_naissance):
    pass

def ajouter_livre(session, titre, annee, auteur_id):
    pass

def emprunter_livre(session, livre_id, emprunteur):
    pass

def retourner_livre(session, livre_id):
    pass

def lister_disponibles(session):
    pass


# Tests
if __name__ == "__main__":
    engine = create_engine("sqlite:///bibliotheque.db")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Ajoute des données de test
        auteur = ajouter_auteur(session, "J.K. Rowling", date(1965, 7, 31))
        livre = ajouter_livre(session, "Harry Potter à l'école des sorciers", 1997, auteur.id)

        print("Livres disponibles:", lister_disponibles(session))
        emprunter_livre(session, livre.id, "Alice")
        print("Après emprunt:", lister_disponibles(session))
