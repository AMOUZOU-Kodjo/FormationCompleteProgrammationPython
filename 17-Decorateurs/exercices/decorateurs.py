"""
Exercice 17.1 : Collection de décorateurs
Crée les décorateurs suivants :

1. @timer : affiche le temps d'exécution
2. @log_appel : enregistre chaque appel dans un fichier log
3. @memoize : met en cache les résultats (mémoïsation)
4. @validation(types) : vérifie les types des arguments
"""

import time
from functools import wraps

# À compléter
def timer(fonction):
    pass

def log_appel(fonction):
    pass

def memoize(fonction):
    pass

def validation(*types):
    pass


# Tests
@timer
def calcul_long(n):
    time.sleep(0.1)
    return sum(range(n))

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@validation(int, int)
def addition(a, b):
    return a + b


if __name__ == "__main__":
    print(calcul_long(1000))
    print(fibonacci(35))  # rapide grâce à memoize
    print(addition(3, 5))  # OK
    # addition("a", 5)  # devrait lever TypeError
