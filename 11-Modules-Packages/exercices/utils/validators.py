"""
Module de validation
"""

def est_email(valeur: str) -> bool:
    """Vérifie si la valeur ressemble à un email."""
    return "@" in valeur and "." in valeur.split("@")[-1]

def est_tel(valeur: str) -> bool:
    """Vérifie si la valeur ressemble à un numéro de téléphone."""
    chiffres = [c for c in valeur if c.isdigit()]
    return len(chiffres) >= 10
