from Model.Joueur import *
from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from random import randint

def IA(joueur: dict) -> int:
    """
    Fonction qui permet de faire jouer l'intelligence artificielle (IA)..

    :param joueur: Le joueur qui est représenté par l'IA
    :return: La fonction retourne le numéro de colonne où l'IA décide de jouer
    """

    plateauJoueur = getPlateauJoueur(joueur)

    colonnesABloquer = []
    for i in range(len(plateauJoueur[0])):
        colonneAlignementVertical = detecter3verticalIA(plateauJoueur, joueur[const.COULEUR])
        if colonneAlignementVertical != -1:
            colonnesABloquer.append(colonneAlignementVertical)

    colonneAlignementHorizontal = detecter3horizontalIA(plateauJoueur, joueur[const.COULEUR])
    if colonneAlignementHorizontal != -1:
        colonnesABloquer.append(colonneAlignementHorizontal)

    colonneDiagDirect = detecter3diagonaleDirecteIA(plateauJoueur, joueur[const.COULEUR])
    if colonneDiagDirect != -1:
        colonnesABloquer.append(colonneDiagDirect)

    colonneDiagIndirect = detecter3diagonaleIndirecteIA(plateauJoueur, joueur[const.COULEUR])
    if colonneDiagIndirect != -1:
        colonnesABloquer.append(colonneDiagIndirect)

    if colonnesABloquer:
        return colonnesABloquer[0]

    return PlacerPionJoueur(joueur)

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

def detecter3verticalIA(plateau: list, couleur: int) -> int:
    """
    Fonction qui permet de détecter un alignement vertical de 3 pions de la même couleur dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectuer la détection
    :param couleur: La couleur des pions pour lesquels on veut détecter l'alignement
    :return: Le numéro de la colonne où l'alignement vertical de 3 pions est détecté, ou -1 s'il n'y a pas d'alignement
    """
    for i in range(len(plateau[0])):
        modif = True
        for j in range(3, len(plateau)):
            if plateau[j][i] is not None and plateau[j - 1][i] is not None and plateau[j - 2][i] is not None and modif:
                if plateau[j][i].get(const.COULEUR) != couleur and plateau[j - 1][i].get(const.COULEUR) != couleur and plateau[j - 2][i].get(const.COULEUR) != couleur and plateau[j - 3][i] is None:
                    return i
    return -1

def detecter3horizontalIA(plateau: list, couleur: int) -> int:
    """
    Fonction qui permet de détecter un alignement horizontal de 3 pions de la même couleur dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectuer la détection
    :param couleur: La couleur des pions pour lesquels on veut détecter l'alignement.
    :return: Le numéro de la colonne où l'alignement horizontal de 3 pions est détecté, ou -1 s'il n'y a pas d'alignement.
    """
    for i in range(len(plateau)):
        for j in range(len(plateau[i]) - 3):
            if plateau[i][j] is not None and plateau[i][j + 1] is not None and plateau[i][j + 2] is not None and plateau[i][j + 3] is None:
                if plateau[i][j].get(const.COULEUR) != couleur and plateau[i][j + 1].get(const.COULEUR) != couleur and plateau[i][j + 2].get(const.COULEUR) != couleur:
                    return j + 3
    return -1

def detecter3diagonaleDirecteIA(plateau: list, couleur: int) -> int:
    """
    Fonction qui permet de détecter un alignement diagonal direct de 3 pions de la même couleur dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectuer la détection
    :param couleur: La couleur des pions pour lesquels on veut détecter l'alignement.
    :return: Le numéro de la colonne où l'alignement diagonal direct de 3 pions est détecté, ou -1 s'il n'y a pas d'alignement.
    """
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

                if plateau[i][j] is not None and plateau[i + 1][j + 1] is not None and plateau[i + 2][j + 2] is not None and plateau[i + 3][j + 3] is None and modif:

                    if plateau[i][j].get(const.COULEUR) != couleur and plateau[i + 1][j + 1].get(const.COULEUR) != couleur and plateau[i + 2][j + 2].get(const.COULEUR) != couleur:
                        return j + 3
                        modif = False
                        diagonale_trouvee = True
            i += 1
            j += 1

    return -1

def detecter3diagonaleIndirecteIA(plateau: list, couleur: int) -> int:
    """
    Fonction qui permet de détecter un alignement diagonal indirect de 3 pions de la même couleur dans un plateau de jeu.

    :param plateau: Plateau dans lequel on effectuer la détection
    :param couleur: La couleur des pions pour lesquels on veut détecter l'alignement.
    :return: Le numéro de la colonne où l'alignement diagonal indirect de 3 pions est détecté, ou -1 s'il n'y a pas d'alignement.
    """
    for k in range(3, -4, -1):
        i, j = 5, 0
        if k >= 0:
            i -= k
        else:
            j = -k

        diagonale_trouvee = True

        while i >= 3 and j <= 6 and diagonale_trouvee:
            modif = True

            if j + 3 < len(plateau[i]) and i - 3 >= 0:

                if plateau[i][j] is not None and plateau[i - 1][j + 1] is not None and plateau[i - 2][j + 2] is not None and plateau[i - 3][j + 3] is None and modif:

                    if plateau[i][j].get(const.COULEUR) != couleur and plateau[i - 1][j + 1].get(const.COULEUR) != couleur and plateau[i - 2][j + 2].get(const.COULEUR) != couleur:
                        return j + 3
            else:
                diagonale_trouvee = False

            i -= 1
            j += 1

    return -1