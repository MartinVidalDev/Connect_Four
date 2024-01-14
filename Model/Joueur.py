from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from Model.IAJoueur import *
from random import randint



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
    if type(couleur) is not int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    if couleur not in const.COULEURS:
        raise ValueError("construirePion : la couleur (valeur_du_paramètre) n’est pas correcte")

    joueur = { const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}
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

    return joueur[const.COULEUR]

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

def getPlacerPionJoueur(joueur: dict) -> callable:
    """
    Fonction qui permet d'obtenir où le joueur a placé son pion.

    :param joueur: Joueur dont on cherche le placement du pion
    :return: La fonction retourne une fonction
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")

    return joueur[const.PLACER_PION]

def getPionJoueur(joueur: dict) -> dict:
    """
    La fonction construit un pion en utilisant la couleur du joueur.

    :param joueur: Joueur à partir duquel on construit le pion
    :return: Retourne le pion construit
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    """

    if type_joueur(joueur) is not True:
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")

    a = construirePion(getCouleurJoueur(joueur)    )
    return a

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Fonction qui affecte le plateau en paramètre au joueur.

    :param joueur: Joueur auquel on veut affecter le plateau
    :param plateau: Plateau que l'on souhaite affecter
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramètre n'est pas un dictionnaire (joueur)
    :raise TypeError: Si le second paramètre n'est pas un plateau
    """

    if type_joueur(joueur) is not True:
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    if type_plateau(plateau) is not True:
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")

    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fonction: callable) -> None:
    """
    Cette fonction affecte la fonction en paramètres au joueur.

    :param joueur: Joueur auquel on veut affecter la fonction
    :param fonction: Fonction que l'on souhaite affecter au joueur
    :return: Ne retourne rien
    :raise TypeError: Si le paramètre n'est pas un dictionnaire (joueur)
    :raise TypeError: Si le second paramètre n'est pas une fonction
    """

    if type_joueur(joueur) is not True:
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if not callable(fonction):
        raise TypeError("setPlacerPionJoueur : le second paramètre n’est pas une fonction")

    joueur[const.PLACER_PION] = fonction
    return None

def _placerPionJoueur(joueur: dict) -> int:
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

def initialiserIAJoueur(joueur: dict, premier: bool) -> None:
    """
    Fonction qui permet de faire jouer l'IA.

    :param joueur: Joueur que l'on fait jouer
    :param premier: Permet de savoir si le joueur commence (True pour jouer en premier / False pour jouer en deuxième)
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramète ne correspond pas à un joueur
    :raise TypeError: Si le second paramètre ne correspond pas à un booléen
    """

    if type_joueur(joueur) is not True:
        raise TypeError("_PlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if type(premier) is not bool:
        raise TypeError("_PlacerPionJoueur : Le seconde paramètre n'est pas un booléen")

    joueur[const.PLACER_PION] = IA
    return None