"""
Exercice 25.2 : Mini ORM avec métaclasse
Crée une métaclasse ModeleMeta qui :
1. Enregistre le nom de la table (= nom de la classe en minuscules)
2. Collecte les attributs de type Champ dans _champs
3. Ajoute une méthode save() qui génère un INSERT SQL
4. Ajoute une méthode find(id) qui génère un SELECT

Classe Champ : nom, type, nullable, defaut
"""

# À compléter
class Champ:
    def __init__(self, type_champ, nullable=True, defaut=None):
        self.type_champ = type_champ
        self.nullable = nullable
        self.defaut = defaut


class ModeleMeta(type):
    pass


class Utilisateur(metaclass=ModeleMeta):
    id = Champ(int, nullable=False)
    nom = Champ(str)
    email = Champ(str)
    age = Champ(int, nullable=True)


# Tests
if __name__ == "__main__":
    u = Utilisateur()
    u.id = 1
    u.nom = "Alice"
    u.email = "alice@example.com"
    print(u.save())
    # INSERT INTO utilisateur (id, nom, email, age) VALUES (1, 'Alice', 'alice@example.com', NULL)
