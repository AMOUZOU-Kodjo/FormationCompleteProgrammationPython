"""
Exercice 4.1 : Gestionnaire de liste de courses
Crée un programme qui :
1. Demande à l'utilisateur d'ajouter des articles (un par un)
2. Affiche la liste numérotée
3. Permet de supprimer un article par son nom
L'utilisateur tape "stop" pour terminer.
"""

# À compléter
courses = []
while True:
    article = input("Ajoute un article (ou 'stop') : ")
    if article.lower() == "stop":
        break
    # Ajoute l'article à la liste

# Affiche la liste numérotée
