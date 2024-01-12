from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur: int) -> dict:
    """
    Fonction permettant de construire un joueur.

    :param couleur: Permet de choisir la couleur que l'on veut attribuer au joueur.
    :return: La fonction retourne un dictionnaire représentant un joueur dans lequel la couleur sera initialisée avec le paramètre donné
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    if couleur not in const.COULEURS:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")

    joueur = {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}

    return joueur

def getCouleurJoueur(joueur: dict) -> int:
    """
    Fonction qui permet d'obtenir la couleur du joueur passé en paramètre.

    :param joueur: Joueur dont on cherche la couleur
    :return: La fonction retourne la couleur du joueur
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")

    couleurJoueur = joueur.get(const.COULEUR)
    return couleurJoueur

def getPlateauJoueur(joueur: dict) -> list:
    """
    Fonction qui permet d'obtenir le plateau du joueur passé en paramètre.

    :param joueur: Joueur dont on cherche le plateau
    :return: La fonction retourne le plateau du joueur
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")

    plateauJoueur = joueur.get(const.PLATEAU)
    return plateauJoueur

def getPlacerPionJoueur(joueur: dict) -> callable:
    """
    Fonction qui permet d'obtenir où le joueur a placé son pion.

    :param joueur: Joueur dont on cherche le placement du pion
    :return: La fonction retourne une fonction
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")

    placerPionJoueur = joueur.get(const.PLACER_PION)
    return placerPionJoueur

def getPionJoueur(joueur: dict) -> dict:
    """
    La fonction construit un pion en utilisant la couleur du joueur.

    :param joueur: Joueur à partir duquel on construit le pion
    :return: Retourne le pion construit
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")

    pionConstruitJoueur = construirePion(getCouleurJoueur(joueur))
    return pionConstruitJoueur