# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur : int) -> dict:
    """
    Fonction permettant de construire un pion

    :param couleur: Couleur du pion à construire
    :return: Dictionnaire représentant un pion
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type(couleur) is not int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")

    if couleur not in const.COULEURS:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")

    pion = { const.COULEUR: couleur, const.ID: None}
    return pion

def getCouleurPion(pion: dict) -> int:
    """
    Fonction permettant d'obtenir la couleur du pion

    :param pion: Pion dont ont récupère la couleur
    :return: Entier représentant la couleur du pion passé en paramètre
    :raise TypeError: Si le paramètre n'est pas un dictionnaire
    """
    if type_pion(pion) is not True:
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion ")

    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur: int) -> None:
    """
    Fonction permettant de changer la couleur du pion

    :param pion: Pion sur lequel on effectue la modification de couleur
    :param couleur: Nouvelle couleur choisie pour le pion
    :return: Ne retourne rien
    :raise TypeError: Si le paramètre pion n'est pas un dictionnaire
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si le paramètre couleur ne représente pas une couleur
    """
    if type_pion(pion) is not True:
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    if type(couleur) is not int:
        raise TypeError("setCouleurPion : setCouleurPion : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError("setCouleurPion : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur")

    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> int:
    """
    Fonction permettant d'obtenir l'identifiant d'un pion

    :param pion: Pion sur lequel on cherche l'identifiant
    :return: Entier représentant l'identifiant du pion
    :raise TypeError: Si le paramètre n'est pas un dictionnaire
    """
    if type_pion(pion) is not True:
        raise TypeError("getIdPion : Le premier paramètre n’est pas un pion")

    return pion[const.ID]

def setIdPion(pion: dict, val: int) -> None:
    """
    Fonction permettant de modifier l'identifiant d'un pion

    :param pion: Pion sur lequel on effectue la modification de l'identifiant
    :param val: Nouvelle valeur de l'identifiant
    :return: Ne retourne rien
    :raise TypeError: Si le paramètre pion n'est pas un dictionnaire
    :raise TypeError: Si le paramètre valeur n'est pas un entier
    """
    if type_pion(pion) is not True:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    if type(val) != int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier")
    pion[const.ID] = val
    return None