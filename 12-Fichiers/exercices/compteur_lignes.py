"""
Exercice 12.2 : Analyseur de fichiers texte
Écris un programme qui :
1. Demande le nom d'un fichier à l'utilisateur
2. Affiche le nombre de lignes, mots et caractères
3. Affiche les 5 lignes les plus longues
4. Gère les erreurs (fichier introuvable, etc.)
"""

# À compléter
nom_fichier = input("Nom du fichier : ")

try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        # Analyse ici
        pass
except FileNotFoundError:
    print(f"Fichier '{nom_fichier}' introuvable.")
