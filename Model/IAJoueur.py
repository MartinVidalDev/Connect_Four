from Model.Joueur import *
from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from random import randint


def PlacerPionJoueur(joueur: dict) -> int:
    """
    Cette fonction permet de choisir une colonne aléatoirement dans mon plateau.

    :param joueur: Joueur dont on veut tirer aléatoirement la colonne
    :return: Retourne le numéro de la colonne
    :raise TypeError: Si le premier paramètre n'est pas un pion
    """
    if type_joueur(joueur) is not True:
        raise TypeError("_PlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")

    modif = False
    plateauJoueur = getPlateauJoueur(joueur)
    tirage = randint(0, const.NB_COLUMNS - 1)

    while modif == False:
        if plateauJoueur[0][tirage] is None:
            modif = True
        else:
            tirage = randint(0, const.NB_COLUMNS - 1)

    return tirage

def getPlateauJoueur(joueur: dict) -> list:
    """
    Fonction qui permet d'obtenir le plateau du joueur passé en paramètre.

    :param joueur: Joueur dont on cherche le plateau
    :return: La fonction retourne le plateau du joueur
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")

    return joueur[const.PLATEAU]