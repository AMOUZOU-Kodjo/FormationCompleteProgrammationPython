"""
Exercice 22.2 : Classe générique avec TypeVar
Crée une classe Pile générique avec TypeVar.
"""

from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")

# À compléter
class Pile(Generic[T]):
    def __init__(self) -> None:
        pass

    def empiler(self, element: T) -> None:
        pass

    def depiler(self) -> Optional[T]:
        pass

    def sommet(self) -> Optional[T]:
        pass

    def __len__(self) -> int:
        pass

    def __bool__(self) -> bool:
        pass


# Tests
if __name__ == "__main__":
    pile_int: Pile[int] = Pile()
    pile_int.empiler(1)
    pile_int.empiler(2)
    pile_int.empiler(3)
    print(pile_int.depiler())  # 3
    print(len(pile_int))       # 2

    pile_str: Pile[str] = Pile()
    pile_str.empiler("a")
    print(pile_str.sommet())  # "a"
