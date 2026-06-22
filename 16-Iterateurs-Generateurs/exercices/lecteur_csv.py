"""
Exercice 16.2 : Lecteur CSV avec générateur
Crée un générateur lire_csv(nom_fichier) qui :
1. Lit un fichier CSV ligne par ligne
2. Découpe chaque ligne par la virgule
3. Convertit les nombres en int/float quand possible
4. Yield chaque ligne transformée

Teste-le avec le fichier data.csv créé au préalable.
"""

# À compléter
def lire_csv(nom_fichier):
    pass

# Création du fichier de test
with open("data.csv", "w") as f:
    f.write("nom,age,note\n")
    f.write("Alice,25,15.5\n")
    f.write("Bob,30,12.0\n")
    f.write("Charlie,22,17.5\n")

# Test
for ligne in lire_csv("data.csv"):
    print(ligne)
