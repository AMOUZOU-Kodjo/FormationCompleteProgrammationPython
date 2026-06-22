"""
Exercice 18.2 : Connexion simulée à une base de données
Crée un context manager ConnexionBase qui simule :
- __enter__() : établit la connexion, crée un curseur
- __exit__() : ferme le curseur, ferme la connexion

La classe ConnexionBase :
- Attributs : hote, port, nom_bd, connecte (bool)
- Méthode : requete(sql) → résultat simulé
"""

# À compléter
class ConnexionBase:
    def __init__(self, hote="localhost", port=3306, nom_bd="test"):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def requete(self, sql):
        pass


# Test
if __name__ == "__main__":
    with ConnexionBase("serveur1", 5432, "ma_base") as db:
        resultat = db.requete("SELECT * FROM utilisateurs")
        print(resultat)
    # "Connexion fermée" doit s'afficher
