from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *

p = construirePlateau()
print(p)
pion = construirePion(const.JAUNE)
line = placerPionPlateau(p, pion, 2)
print("Placement d’un pion en colonne 2. Numéro de ligne :", line)
print(p)

# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")

def toStringPlateau(plateau):
    """
    Fonction permettant d'afficher un plateau de puissance 4 dans la console

    :param plateau: Plateau que l'on veut transformer en chaîne de caractères (mode graphique)
    :return: Retourne le plateau en chaîne de caractères
    """
    res = ""

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            res += "|" + " "
        res += "|\n"

    for i in range(len(plateau[0]) * 2 + 1):
        res += "-"
    res += "\n"

    for i in range(len(plateau[0])):
        res += " " + str(i)

    return res