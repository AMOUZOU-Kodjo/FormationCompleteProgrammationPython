"""
Exercice 14.1 : Système de véhicules
Crée une hiérarchie de classes :

Classe de base : Vehicule
- Attributs : marque, modele, annee, vitesse_max
- Méthode : description() → "Marque Modèle (année)"
- Méthode : calculer_temps_trajet(distance_km) → heures

Sous-classes :
- Voiture : nb_portes, climatisation (bool)
  - surcharge de description()
- Moto : type_moteur, a_sidecar (bool)
  - surcharge de description()
- Camion : capacite_tonnes
  - méthode : charger(tonnes), decharger(tonnes)
"""

# À compléter
class Vehicule:
    pass

class Voiture(Vehicule):
    pass

class Moto(Vehicule):
    pass

class Camion(Vehicule):
    pass


# Tests
if __name__ == "__main__":
    v = Voiture("Toyota", "Corolla", 2020, 180, 5, True)
    m = Moto("Yamaha", "MT-07", 2022, 220, "Bi-cylindre", False)
    c = Camion("Renault", "Magnum", 2019, 130, 20)

    for vehicule in [v, m, c]:
        print(vehicule.description())
        print(f"  Temps pour 300 km : {vehicule.calculer_temps_trajet(300):.2f}h")
