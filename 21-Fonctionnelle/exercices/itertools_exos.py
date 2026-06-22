"""
Exercice 21.2 : Exercices avec itertools
Utilise itertools pour résoudre ces problèmes :

1. cycle + islice : générer les 10 premiers éléments de la séquence infie A, B, C, A, B, C, ...
2. permutations : lister tous les mots de 2 lettres possibles avec "ABC"
3. combinations : lister toutes les combinaisons de 2 lettres avec "ABC"
4. product : générer toutes les plaques d'immatriculation à 3 chiffres
5. groupby : grouper des mots par leur première lettre
6. chain : concaténer 3 listes en une seule
"""

from itertools import cycle, islice, permutations, combinations, product, groupby, chain

# À compléter

# 1. Série cyclique
serie = list(islice(cycle(["A", "B", "C"]), 10))
print("Série cyclique:", serie)

# 2. Permutations de 2 lettres
perms = [''.join(p) for p in permutations("ABC", 2)]
print("Permutations:", perms)

# 3. Combinaisons de 2 lettres
combs = [''.join(c) for c in combinations("ABC", 2)]
print("Combinaisons:", combs)

# 4. Plaques 3 chiffres
plaques = list(product("0123456789", repeat=3))
print(f"Nombre de plaques: {len(plaques)}")  # 1000

# 5. Grouper par première lettre
mots = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
# À compléter
for lettre, groupe in groupby(sorted(mots), key=lambda m: m[0]):
    print(f"{lettre}: {list(groupe)}")

# 6. Concaténer 3 listes
listes = [[1, 2], [3, 4], [5, 6]]
concat = list(chain.from_iterable(listes))
print("Concat:", concat)
