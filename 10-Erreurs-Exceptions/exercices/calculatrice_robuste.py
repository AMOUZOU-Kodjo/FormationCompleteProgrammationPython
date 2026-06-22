"""
Exercice 10.2 : Calculatrice robuste
Reprend la calculatrice des exercices précédents avec :
- Gestion des ValueError (mauvaise saisie)
- Gestion des ZeroDivisionError
- Gestion des KeyboardInterrupt (Ctrl+C)
- Boucle continue jusqu'à "q" pour quitter
"""

# À compléter
while True:
    try:
        expr = input("Calcul (ex: 3 + 5) ou 'q' pour quitter : ")
        if expr.lower() == 'q':
            break
        # Parse et exécute le calcul
    except KeyboardInterrupt:
        print("\nAu revoir !")
        break
