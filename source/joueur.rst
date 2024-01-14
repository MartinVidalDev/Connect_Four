Model.Joueur
==========

    Fonctions permettant de gérer le joueur.

    Exemple d'utilisation :

    .. code-block:: python

        from Model.Constantes import *
        from Model.Plateau import construireJoueur

        # Création d'un joueur
        joueur = construireJoueur(const.COULEUR)

.. autofunction:: Model.Joueur.construireJoueur
.. autofunction:: Model.Joueur.getCouleurJoueur
.. autofunction:: Model.Joueur.getPlateauJoueur
.. autofunction:: Model.Joueur.getPlacerPionJoueur
.. autofunction:: Model.Joueur.getPionJoueur
.. autofunction:: Model.Joueur.setPlateauJoueur
.. autofunction:: Model.Joueur.setPlacerPionJoueur
.. autofunction:: Model.Joueur._placerPionJoueur
.. autofunction:: Model.Joueur.initialiserIAJoueur