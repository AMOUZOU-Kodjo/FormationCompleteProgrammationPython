"""
Exercice 28.1 : Système de logging avancé
Configure un système de logging complet :

1. Logger principal nommé "mon_app"
2. Handler console pour les messages INFO et plus
3. Handler fichier "app.log" pour tous les messages (DEBUG+)
4. Handler fichier "errors.log" pour ERROR et CRITICAL uniquement
5. Format : [DATE] NIVEAU module — message
6. Crée un décorateur @log_appel avec logging
"""

import logging
from functools import wraps

# À compléter
def configurer_logging():
    pass

logger = logging.getLogger("mon_app")

def log_appel(func):
    pass


# Test
@log_appel
def diviser(a, b):
    return a / b

@log_appel
def traiter_donnees(valeurs):
    return [v * 2 for v in valeurs]

if __name__ == "__main__":
    configurer_logging()
    logger.info("Application démarrée")
    print(diviser(10, 2))
    print(traiter_donnees([1, 2, 3]))
    try:
        diviser(10, 0)
    except ZeroDivisionError:
        logger.error("Tentative de division par zéro")
    logger.info("Application terminée")
