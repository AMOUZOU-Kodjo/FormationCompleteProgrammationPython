"""
Exercice 24.1 : Threading — Téléchargements simulés
Crée un programme avec ThreadPoolExecutor qui télécharge
simultanément plusieurs fichiers (simulés avec time.sleep).

Compare le temps séquentiel vs threading pour 10 fichiers de 1s chacun.
"""

import time
from concurrent.futures import ThreadPoolExecutor

# À compléter
def telecharger_fichier(nom_fichier):
    pass

def sequentiel(fichiers):
    pass

def avec_threading(fichiers, max_workers=4):
    pass


if __name__ == "__main__":
    fichiers = [f"fichier_{i}.txt" for i in range(10)]

    start = time.time()
    sequentiel(fichiers)
    t_sequentiel = time.time() - start

    start = time.time()
    avec_threading(fichiers, max_workers=4)
    t_threading = time.time() - start

    print(f"Séquentiel : {t_sequentiel:.2f}s")
    print(f"Threading (4) : {t_threading:.2f}s")
    print(f"Accélération : {t_sequentiel/t_threading:.1f}x")
