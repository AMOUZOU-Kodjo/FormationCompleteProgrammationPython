"""
Projet final : Template pour démarrer
Structure de base pour le projet final au choix.

Remplace ce fichier par ton projet final complet.
"""

import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Point d'entrée du projet final."""
    logger.info("Projet final démarré")
    print("Bienvenue dans le projet final de la formation Python !")


if __name__ == "__main__":
    main()
