"""
Exercice 17.2 : Contrôle d'accès par décorateur
Crée un décorateur @acces_requis(niveau) qui :
- Vérifie si l'utilisateur a le niveau d'accès suffisant
- Utilise une variable globale utilisateur = {"nom": "...", "role": "..."}
- Lève une PermissionError si l'accès est refusé

Niveaux : "admin" > "editeur" > "lecteur"
"""

# À compléter
UTILISATEUR = {"nom": "Alice", "role": "editeur"}

def acces_requis(niveau_minimum):
    pass


# Tests
@acces_requis("lecteur")
def voir_donnees():
    return "Données visibles"

@acces_requis("editeur")
def modifier_donnees():
    return "Données modifiées"

@acces_requis("admin")
def supprimer_donnees():
    return "Données supprimées"

if __name__ == "__main__":
    print(voir_donnees())
    print(modifier_donnees())
    # print(supprimer_donnees())  # PermissionError pour Alice (editeur)
