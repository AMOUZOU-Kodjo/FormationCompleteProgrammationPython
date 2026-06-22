"""
Exercice 34.1 : Analyse d'un dataset
Analyse le dataset Titanic (disponible en ligne ou crée un dataset factice).

Étapes :
1. Charge les données dans un DataFrame
2. Affiche les infos de base (head, info, describe)
3. Nettoie les données (valeurs manquantes, doublons)
4. Analyse : moyenne d'âge par classe, taux de survie par sexe
5. Crée des visualisations simples (avec matplotlib)

Dataset factice fourni ci-dessous si pas de fichier externe.
"""

import pandas as pd
import numpy as np

# Dataset factice
np.random.seed(42)
n = 100
data = {
    "passenger_id": range(1, n+1),
    "classe": np.random.choice([1, 2, 3], n),
    "age": np.random.randint(1, 80, n).astype(float),
    "sexe": np.random.choice(["M", "F"], n),
    "tarif": np.random.uniform(5, 100, n).round(2),
    "survived": np.random.choice([0, 1], n, p=[0.6, 0.4]),
}
df = pd.DataFrame(data)
# Ajoute des valeurs manquantes
df.loc[np.random.choice(n, 10), "age"] = np.nan

# À compléter
def analyser_dataset(df):
    pass

def nettoyer_donnees(df):
    pass

def statistiques(df):
    pass

if __name__ == "__main__":
    analyser_dataset(df)
    print("\nStatistiques:")
    statistiques(df)
