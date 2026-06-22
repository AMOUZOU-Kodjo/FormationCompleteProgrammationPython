"""
Exercice 18.1 : Collection de context managers
Crée les context managers suivants :

1. Chronometre : mesure et affiche le temps d'exécution du bloc
2. RedirectionSortie(fichier) : redirige temporairement print() vers un fichier
3. RepertoireTemporaire : crée un dossier temporaire et le supprime à la sortie
4. IgnorerException(*exceptions) : ignore les exceptions spécifiées
"""

import os
import time
import shutil
import tempfile
from contextlib import contextmanager

# À compléter
class Chronometre:
    pass

@contextmanager
def redirection_sortie(fichier):
    pass

@contextmanager
def repertoire_temporaire():
    pass

@contextmanager
def ignorer_exception(*exceptions):
    pass


# Tests
if __name__ == "__main__":
    with Chronometre():
        time.sleep(0.5)

    with ignorer_exception(ValueError, ZeroDivisionError):
        x = int("abc")  # ignoré
        y = 1 / 0       # ignoré
    print("Ça continue !")
