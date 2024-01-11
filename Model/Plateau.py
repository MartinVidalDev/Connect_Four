from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Fonction permettant de créer un plateau de jeu vide

    :return: Tableau 2D vide
    """
    plateau = []
    for i in range(const.NB_LINES):
        row = []
        for j in range(const.NB_COLUMNS):
            row.append(None)
        plateau.append(row)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, numcol: int) -> int:
    """
    Fonction permettant de placer un pion dans notre plateau de jeu

    :param plateau: Plateau dans lequel on ajoute le pion
    :param pion: Pion que l'on place dans le plateau
    :param numcol: Numéro de la colonne dans laquelle on place le pion
    :return: La fonction retourne le numéro de ligne où se retrouve le pion
             (soit tout en bas, soit au dessus d'un autre pion, soit tout en haut de la colonne).
             Si la colonne est déjà pleine , la fonction retourne -1.
    :raise TypeError : Si le premier paramètre n'est pas un plateau
    :raise TypeError : Si le deuxième paramètre n'est pas un pion
    :raise TypeError : Si la valeur de numcol n'est pas un entier
    """
    if type_plateau(plateau) != True:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion) != True:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(numcol) != int:
        raise TypeError("placerPionPlateau : La valeur de la colonne (valeur_du_paramètre) n’est pas correcte")

    i = len(plateau)-1
    res = i + 1
    modif = False
    j = 0
    if plateau[j][numcol] != None:
        res = -1
        modif = True

    while i > -1 and modif == False:
        if plateau[i][numcol] == None:
            plateau[i][numcol] = pion
            modif = True
        i -= 1
        res -= 1
    return res

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter un alignement horizontal de 4 pions de la même couleur côte à côte dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectue la rcherche de l'alignement horizontal
    :param couleur: Permet de choisir la couleur des pions dont on veux savoir s'il y a alignement horizontal
    :return: Si la fonction retourne une liste vide, il n'y pas l'alignement horizontal des pions de même couleur, Sinon elle retourne avec les 4 pions.
             Si il y a plusieurs lignes d'alignement alors la fonction retourne une liste de liste contenant les pions.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si l'entier de couleur ne représente pas une couleur
    """

    if type_plateau(plateau) != True:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : setCouleurPion : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4horizontalPlateau : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur")

    res = []

    for i in range(len(plateau)):
        modif = True
        for j in range(len(plateau[i])):

            if j + 3 < len(plateau[i]) and plateau[i][j] is not None and plateau[i][j+1] is not None and plateau[i][j+2] is not None and plateau[i][j+3] is not None and modif:
                if plateau[i][j].get(const.COULEUR) == couleur and plateau[i][j+1].get(const.COULEUR) == couleur and plateau[i][j+2].get(const.COULEUR) == couleur and plateau[i][j+3].get(const.COULEUR) == couleur:
                    listeTemp = plateau[i][j:j+4]
                    res.append(listeTemp)
                    modif = False
    return res