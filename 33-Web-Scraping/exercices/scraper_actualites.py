"""
Exercice 33.1 : Scraper d'actualités
Crée un scraper qui :

1. Récupère les articles d'un site d'actualités (ex: Hacker News)
   https://news.ycombinator.com/
2. Extrait : titre, lien, score, auteur
3. Sauvegarde dans un fichier JSON
4. Affiche les 5 articles les mieux notés

Utilise requests + BeautifulSoup.
Ajoute un délai entre les requêtes et des User-Agent.
"""

import requests
from bs4 import BeautifulSoup
import json
import time

# À compléter
class ScraperActualites:
    def __init__(self, url):
        pass

    def recuperer_articles(self):
        pass

    def top_articles(self, n=5):
        pass

    def sauvegarder(self, fichier="articles.json"):
        pass


if __name__ == "__main__":
    scraper = ScraperActualites("https://news.ycombinator.com/")
    articles = scraper.recuperer_articles()
    print(f"Récupéré {len(articles)} articles")

    for article in scraper.top_articles(5):
        print(f"[{article['score']}] {article['titre'][:50]}...")

    scraper.sauvegarder()
