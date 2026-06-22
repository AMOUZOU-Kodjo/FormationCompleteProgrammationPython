"""
Exercice 16.1 : Itérateurs et générateurs

1. Crée un itérateur Paire(max) qui génère les nombres pairs jusqu'à max
2. Crée un générateur fibonacci(n) qui génère les n premiers nombres de Fibonacci
3. Crée un générateur plages(n) qui génère les plages [0,1], [1,2], [2,3], ...
4. Crée un générateur infini cycle(iterable) qui répète l'itérable indéfiniment
"""

# À compléter
class Paire:
    pass

def fibonacci_gen(n):
    pass

def plages(n):
    pass

def cycle(iterable):
    pass


# Tests
if __name__ == "__main__":
    print("Paires :", list(Paire(10)))  # [0, 2, 4, 6, 8]
    print("Fibonacci :", list(fibonacci_gen(10)))
    print("Plages :", list(plages(4)))  # [(0,1), (1,2), (2,3), (3,4)]
