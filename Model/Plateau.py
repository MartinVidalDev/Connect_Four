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

def placerPionPlateau(plateau: list, pion: dict, colonne: int) -> int:
    """
    Fonction permettant de placer un pion dans notre plateau de jeu

    :param plateau: Plateau dans lequel on ajoute le pion
    :param pion: Pion que l'on place dans le plateau
    :param colonne: Numéro de la colonne dans laquelle on place le pion
    :return: La fonction retourne le numéro de ligne où se retrouve le pion
             (soit tout en bas, soit au dessus d'un autre pion, soit tout en haut de la colonne).
             Si la colonne est déjà pleine , la fonction retourne -1.
    :raise TypeError : Si le premier paramètre n'est pas un plateau
    :raise TypeError : Si le deuxième paramètre n'est pas un pion
    :raise TypeError : Si la valeur de colonne n'est pas un entier
    :raise ValueError : Si la valeur de colonne n'est pas une colonne valide
    """
    if type_plateau(plateau) is not True:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion) is not True:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion")
    if type(colonne) is not int:
        raise TypeError("placerPionPlateau : La valeur de la colonne (valeur_du_paramètre) n’est pas correcte")
    if colonne >= 7:
        raise ValueError("placerPionPlateau : placerPionPlateau : La valeur de la colonne (valeur_du_paramètre) n’est pas correcte")

    res = 0

    if plateau[0][colonne] is None:
        plateau[0][colonne] = pion

    else:
        res = -1

    for lignes in range(1, const.NB_LINES):

        if plateau[lignes][colonne] is None:
            plateau[lignes][colonne] = pion
            plateau[lignes - 1][colonne] = None
            res = lignes

    return res

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter un alignement horizontal de 4 pions de la même couleur côte à côte dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectue la recherche de l'alignement horizontal
    :param couleur: Permet de choisir la couleur des pions dont on veux savoir s'il y a alignement horizontal
    :return: Si la fonction retourne une liste vide, il n'y pas d'alignement horizontal des pions de même couleur, Sinon elle retourne avec les 4 pions aux indices les plus faibles.
             Si il y a plusieurs lignes d'alignement alors la fonction retourne une liste de liste contenant les pions.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si l'entier de couleur ne représente pas une couleur
    """

    if type_plateau(plateau) is not True:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
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
                    res.extend(listeTemp)
                    modif = False
    return res

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter un alignement vertical de 4 pions de la même couleur les uns en dessous des autres dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectue la recherche de l'alignement vertical
    :param couleur: Permet de choisir la couleur des pions dont on veux savoir s'il y a alignement vertical
    :return: Si la fonction retourne une liste vide, il n'y pas d'alignement vertical des pions de même couleur, Sinon elle retourne avec les 4 pions aux indices les plus faibles.
             Si il y a plusieurs lignes d'alignement alors la fonction retourne une liste de liste contenant les pions.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si l'entier de couleur ne représente pas une couleur
    """

    if type_plateau(plateau) != True:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4verticalPlateau : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur")

    res = []

    for i in range(len(plateau[0])):
        modif = True
        for j in range(len(plateau) -3):
            if j + 3 < len(plateau[j]) and plateau[j][i] is not None and modif:
                if plateau[j][i].get(const.COULEUR) == couleur and plateau[j+1][i].get(const.COULEUR) == couleur and plateau[j+2][i].get(const.COULEUR) == couleur and plateau[j+3][i].get(const.COULEUR) == couleur:
                    listeTemp = [plateau[j][i], plateau[j+1][i], plateau[j+2][i], plateau[j+3][i]]
                    res.extend(listeTemp)
                    modif = False
    return res

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter un alignement diagonal de 4 pions de la même couleur alignés en diagonale "directe" (de gauche vers la droite et du haut vers le bas) dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectue la recherche de l'alignement diagonal "direct"
    :param couleur: Permet de choisir la couleur des pions dont on veut savoir s'il y a un alignement diagonal "direct"
    :return: Si la fonction retourne une liste vide, il n'y a pas d'alignement diagonal "direct" des pions de même couleur. Sinon, elle retourne une liste avec les 4 pions alignés en diagonale "directe".
             Si plusieurs diagonales d'alignement sont présentes, la fonction retourne une liste de listes contenant les pions.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si l'entier de couleur ne représente pas une couleur
    """
    if type_plateau(plateau) != True:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4diagonaleDirectePlateau : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur")

    res = []

    for k in range(3, -4, -1):
        i, j = 0, 0
        if k >= 0:
            i = k
        else:
            j = -k

        diagonale_trouvee = False

        while i <= 5 and j <= 6 and not diagonale_trouvee:
            modif = True

            if j + 3 < len(plateau[i]) and i + 3 < len(plateau):

                if plateau[i][j] is not None and plateau[i + 1][j + 1] is not None and plateau[i + 2][j + 2] is not None and plateau[i + 3][j + 3] is not None and modif:

                    if plateau[i][j].get(const.COULEUR) == couleur and plateau[i + 1][j + 1].get(const.COULEUR) == couleur and plateau[i + 2][j + 2].get(const.COULEUR) == couleur and plateau[i + 3][j + 3].get(const.COULEUR) == couleur:

                        listeTemp = [plateau[i][j], plateau[i + 1][j + 1], plateau[i + 2][j + 2], plateau[i + 3][j + 3]]
                        res.extend(listeTemp)
                        modif = False
                        diagonale_trouvee = True
            i += 1
            j += 1

    return res

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter un alignement diagonal de 4 pions de la même couleur alignés en diagonale "indirecte" (de bas en haut et de gauche vers la droite) dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectue la recherche de l'alignement diagonal "indirect"
    :param couleur: Permet de choisir la couleur des pions dont on veut savoir s'il y a un alignement diagonal "indirect"
    :return: Si la fonction retourne une liste vide, il n'y a pas d'alignement diagonal "indirect" des pions de même couleur. Sinon, elle retourne une liste avec les 4 pions alignés en diagonale "indirecte".
             Si plusieurs diagonales d'alignement sont présentes, la fonction retourne une liste de listes contenant les pions.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre couleur n'est pas un entier
    :raise ValueError: Si l'entier de couleur ne représente pas une couleur
    """
    if type_plateau(plateau) != True:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4diagonaleIndirectePlateau : Le second paramètre (valeur_du_second_paramètre) n’est pas une couleur")

    res = []

    for k in range(3, -4, -1):
        i, j = 5, 0
        if k >= 0:
            i -= k
        else:
            j = -k

        diagonale_trouvee = False

        while i >= 3 and j <= 6 and not diagonale_trouvee:
            modif = True

            if j + 3 < len(plateau[i]) and i - 3 >= 0:

                if plateau[i][j] is not None and plateau[i - 1][j + 1] is not None and plateau[i - 2][j + 2] is not None and plateau[i - 3][j + 3] is not None and modif:

                    if plateau[i][j].get(const.COULEUR) == couleur and plateau[i - 1][j + 1].get(const.COULEUR) == couleur and plateau[i - 2][j + 2].get(const.COULEUR) == couleur and plateau[i - 3][j + 3].get(const.COULEUR) == couleur:

                        listeTemp = [plateau[i][j], plateau[i - 1][j + 1], plateau[i - 2][j + 2], plateau[i - 3][j + 3]]
                        res.extend(listeTemp)
                        modif = False
                        diagonale_trouvee = True
            i -= 1
            j += 1

    return res

def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction permettant d'obtenir toutes les séries de pions gagnants.

    :param plateau: Plateau dans lequel on cherche les sérions de pions gagnants.
    :return: La fonction retourne une liste contenant toutes les séries gagnantes. Chaque série gagnante est stockée dans une sous-liste de la liste retournée.
             Si il n'y a pas de séries gagnantes, alors la fonction ne retourne rien.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    """
    if type_plateau(plateau) is not True:
        raise TypeError("getPionsGagnantsPlateau : Le premier paramètre ne correspond pas à un plateau")

    listeSeriesPionsAlignes = []

    for i in const.COULEURS:
        listeSeriesPionsAlignes.extend(detecter4horizontalPlateau(plateau, i))
        listeSeriesPionsAlignes.extend(detecter4verticalPlateau(plateau, i))
        listeSeriesPionsAlignes.extend(detecter4diagonaleDirectePlateau(plateau, i))
        listeSeriesPionsAlignes.extend(detecter4diagonaleIndirectePlateau(plateau, i))

    return listeSeriesPionsAlignes

def isRempliPlateau(plateau: list) -> bool:
    """
    Fonction permmettant de savoir si le plateau de jeu est rempli.

    :param plateau: Plateau dans lequel on cherche à savoir s'il est rempli ou non.
    :return: La fonction retourne True s'il est rempli, sinon elle retourne False.
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    """

    if type_plateau(plateau) is not True:
        raise TypeError("isRempliPlateau : Le premier paramètre ne correspond pas à un plateau")

    plateauRempli = True
    i = 0
    while i < len(plateau) and plateauRempli:
        for j in range(len(plateau[i])):
            if plateau[i][j] is None:
                plateauRempli = False
        i += 1

    return plateauRempli