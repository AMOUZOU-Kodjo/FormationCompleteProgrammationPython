"""
Exercice 23.2 : File d'attente asynchrone (Worker Pool)
Crée un système de workers asynchrones avec asyncio.Queue.

- Producteur : génère des tâches et les met dans la file
- Travailleurs (workers) : consomment les tâches depuis la file
- Limite le nombre de workers simultanés à 3
- Affiche la progression
"""

import asyncio
import random

# À compléter
async def producteur(queue, n_taches):
    pass

async_travailleur = """
async def travailleur(travailleur_id, queue):
    pass
"""

async def main():
    queue = asyncio.Queue(maxsize=10)
    n_taches = 20
    n_workers = 3

    # Lance le producteur et les workers
    producteur_task = asyncio.create_task(producteur(queue, n_taches))
    workers = [asyncio.create_task(travailleur(i, queue)) for i in range(n_workers)]

    await asyncio.gather(producteur_task, *workers)

if __name__ == "__main__":
    asyncio.run(main())
