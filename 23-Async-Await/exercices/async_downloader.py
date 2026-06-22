"""
Exercice 23.1 : Téléchargeur web asynchrone
Crée un programme qui télécharge plusieurs URLs en parallèle.

Fonctions :
- telecharger_url(url) : simule un téléchargement avec asyncio.sleep
- telecharger_urls(urls) : télécharge toutes les URLs avec asyncio.gather
- ajouter_timeout(coroutine, secondes) : ajoute un timeout
- avec_progress(urls) : affiche la progression des téléchargements
"""

import asyncio
import time

# URLs simulées
URLS = [
    "https://api.example.com/data1",
    "https://api.example.com/data2",
    "https://api.example.com/data3",
    "https://api.example.com/data4",
    "https://api.example.com/data5",
]

# À compléter
async def telecharger_url(url):
    pass

async def telecharger_urls(urls):
    pass

async def avec_progress(urls):
    pass


# Tests
async def main():
    start = time.time()
    resultats = await telecharger_urls(URLS)
    duree = time.time() - start
    print(f"Téléchargé {len(resultats)} URLs en {duree:.2f}s")

    # Version avec progression
    await avec_progress(URLS)

if __name__ == "__main__":
    asyncio.run(main())
