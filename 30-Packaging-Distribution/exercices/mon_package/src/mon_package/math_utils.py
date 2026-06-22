def moyenne(*nombres):
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)

def mediane(*nombres):
    if not nombres:
        return 0
    triee = sorted(nombres)
    n = len(triee)
    milieu = n // 2
    if n % 2 == 0:
        return (triee[milieu - 1] + triee[milieu]) / 2
    return triee[milieu]

def factorielle(n):
    if n < 0:
        raise ValueError("Pas de factorielle négative")
    if n <= 1:
        return 1
    return n * factorielle(n - 1)
