"""
Module mathématique de la bibliothèque utils
"""

def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("Pas de factorielle négative")
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    suite = [0, 1]
    for _ in range(2, n):
        suite.append(suite[-1] + suite[-2])
    return suite
