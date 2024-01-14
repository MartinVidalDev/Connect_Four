Model.Plateau
==========

    Fonctions permettant de gérer le plateau du jeu.

    Exemple d'utilisation :

    .. code-block:: python

        from Model.Constantes import *
        from Model.Plateau import construirePlateau

        # Création d'un plateau
        plateau = construirePlateau()

.. autofunction:: Model.Plateau.construirePlateau
.. autofunction:: Model.Plateau.placerPionPlateau
.. autofunction:: Model.Plateau.detecter4horizontalPlateau
.. autofunction:: Model.Plateau.detecter4verticalPlateau
.. autofunction:: Model.Plateau.detecter4diagonaleDirectePlateau
.. autofunction:: Model.Plateau.detecter4diagonaleIndirectePlateau
.. autofunction:: Model.Plateau.getPionsGagnantsPlateau
.. autofunction:: Model.Plateau.isRempliPlateau