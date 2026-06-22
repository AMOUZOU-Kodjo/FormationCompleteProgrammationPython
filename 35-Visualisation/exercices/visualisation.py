"""
Exercice 35.1 : Visualisation de données
Crée les visualisations suivantes à partir du dataset Titanic (ou factice) :

1. Histogramme de la distribution des âges
2. Boxplot des âges par classe
3. Taux de survie par sexe (barres)
4. Nuage de points âge vs tarif, coloré par survie
5. Heatmap des corrélations
6. Sauvegarde toutes les figures dans un dossier "charts/"
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Dataset factice
np.random.seed(42)
n = 200
data = {
    "age": np.random.randint(1, 80, n).astype(float),
    "classe": np.random.choice([1, 2, 3], n),
    "sexe": np.random.choice(["M", "F"], n),
    "tarif": np.random.uniform(5, 100, n).round(2),
    "survived": np.random.choice([0, 1], n, p=[0.6, 0.4]),
}
df = pd.DataFrame(data)

os.makedirs("charts", exist_ok=True)

# À compléter
def histogramme_age(df):
    plt.figure(figsize=(8, 5))
    # Crée l'histogramme
    plt.savefig("charts/age_distribution.png")
    plt.close()

def boxplot_age_classe(df):
    pass

def survie_par_sexe(df):
    pass

def scatter_age_tarif(df):
    pass

def heatmap_correlations(df):
    pass


if __name__ == "__main__":
    histogramme_age(df)
    boxplot_age_classe(df)
    survie_par_sexe(df)
    scatter_age_tarif(df)
    heatmap_correlations(df)
    print("Graphiques sauvegardés dans charts/")
