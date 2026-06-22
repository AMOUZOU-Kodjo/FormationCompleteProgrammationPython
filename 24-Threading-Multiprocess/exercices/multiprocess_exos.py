"""
Exercice 24.2 : Multiprocessing — Calculs intensifs
Calcule la somme des nombres premiers jusqu'à 100 000
en parallèle avec ProcessPoolExecutor.

Compare séquentiel vs multiprocessing (4 process).
"""

import time
import math
from concurrent.futures import ProcessPoolExecutor

# À compléter
def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def somme_premiers_jusqua(limite):
    pass

def sequentiel(limite):
    pass

def avec_multiprocess(limite, n_process=4):
    pass


if __name__ == "__main__":
    LIMITE = 100000

    start = time.time()
    resultat_seq = sequentiel(LIMITE)
    t_seq = time.time() - start
    print(f"Séquentiel : {resultat_seq} en {t_seq:.2f}s")

    start = time.time()
    resultat_mp = avec_multiprocess(LIMITE, 4)
    t_mp = time.time() - start
    print(f"Multiprocess (4) : {resultat_mp} en {t_mp:.2f}s")
    print(f"Accélération : {t_seq/t_mp:.1f}x")
