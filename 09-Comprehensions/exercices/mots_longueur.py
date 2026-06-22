"""
Exercice 9.2 : Analyse de texte avec compréhensions
À partir de la phrase donnée, utilise des compréhensions pour :
1. Créer une liste des longueurs de chaque mot
2. Créer une liste des mots de plus de 4 lettres
3. Créer un dictionnaire {mot: len(mot)}
4. Créer un ensemble des premières lettres de chaque mot
"""

phrase = "Python est un langage de programmation puissant et polyvalent"
mots = phrase.split()

# À compléter
longueurs = []    # [6, 3, 2, 7, 2, ...]
mots_long = []    # mots de plus de 4 lettres
longueur_par_mot = {}  # {"Python": 6, "est": 3, ...}
premieres_lettres = set()  # {"P", "e", "u", "l", ...}
