"""
Module de manipulation de chaînes
"""

def inverser(s: str) -> str:
    """Retourne la chaîne inversée."""
    return s[::-1]

def compter_mots(texte: str) -> int:
    """Retourne le nombre de mots."""
    return len(texte.split())
