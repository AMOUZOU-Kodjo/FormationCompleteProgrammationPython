"""
Exercice 20.2 : Analyseur de fichiers log
Analyse un fichier de log Apache/Nginx avec regex pour extraire :
1. Les adresses IP
2. Les dates/heures
3. Les codes HTTP (200, 404, 500, etc.)
4. Les URLs demandées
5. Compter le nombre d'occurrences de chaque code HTTP

Exemple de ligne :
192.168.1.1 - - [15/Jan/2024:14:30:25 +0100] "GET /index.html HTTP/1.1" 200 1234
"""

import re
from collections import Counter

LOG_EXEMPLE = """192.168.1.1 - - [15/Jan/2024:14:30:25 +0100] "GET /index.html HTTP/1.1" 200 1234
10.0.0.2 - - [15/Jan/2024:14:31:02 +0100] "POST /api/login HTTP/1.1" 401 512
192.168.1.1 - - [15/Jan/2024:14:32:10 +0100] "GET /images/logo.png HTTP/1.1" 304 0
10.0.0.3 - - [15/Jan/2024:14:33:45 +0100] "GET /admin HTTP/1.1" 404 256
192.168.1.2 - - [15/Jan/2024:14:34:00 +0100] "GET /api/data HTTP/1.1" 200 2048
"""

# À compléter
class AnalyseurLog:
    def __init__(self, contenu):
        pass

    def ips(self):
        pass

    def codes_http(self):
        pass

    def urls(self):
        pass

    def statistiques(self):
        pass

    def ips_suspectes(self, seuil=5):
        """IPs avec plus de `seuil` requêtes."""
        pass


# Test
if __name__ == "__main__":
    analyseur = AnalyseurLog(LOG_EXEMPLE)
    print("IPS :", analyseur.ips())
    print("Codes HTTP :", analyseur.codes_http())
    print("Statistiques :", analyseur.statistiques())
