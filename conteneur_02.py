class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min  # Nombre de minutes
        self.sec = sec  # Nombre de secondes

    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    """
    >>> from conteneur_02 import Duree
    >>> d = Duree(3,58)
    >>> d
    <conteneur_02.Duree object at 0x00000000035F2BE0>
    >>> print(d)
    03:58
    """

    def __add__(self, objet_a_ajouter):
        # Sachez que sur le même modèle, il existe les méthodes :
        # __sub__ : surcharge de l'opérateur - ;
        # __mul__ : surcharge de l'opérateur * ;
        # __truediv__ : surcharge de l'opérateur / ;
        # __floordiv__ : surcharge de l'opérateur // (division entière) ;
        # __mod__ : surcharge de l'opérateur % (modulo) ;
        # __pow__ : surcharge de l'opérateur ** (puissance) ;

        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_duree

    """
    >>> from conteneur_02 import Duree
    >>> d = Duree(3,58)
    >>> d + 3
    <conteneur_02.Duree object at 0x000000000362CF28>
    >>> print(d)
    03:58
    >>> d += 3
    >>> print(d)
    04:01
    """

    # Au cas ou on fait l'operation inverse:
    # 3 + d
    # on aura un TypeError: unsupported operand type(s) for +: 'int' and 'Duree'
    # car 3 est de type 'int' et d de type 'Duree'
    # on va donc lui indiquer de gerer cela avec r(everse)add
    def __radd__(self, other):
        return self + other

    """
    >>> from conteneur_02 import Duree
    >>> d = Duree(3,58)
    >>> d1 = d + 3
    >>> d1
    <conteneur_02.Duree object at 0x000000000363CF28>
    >>> print(d1)
    04:01
    >>> d2 = 3 + d
    >>> print(d2)
    04:01
    """

    # Il est également possible de surcharger les opérateurs +=, -=, etc.
    # On préfixe cette fois-ci les noms de méthode que nous avons vus par un i.
    def __iadd__(self, other):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        # On travaille directement sur self cette fois
        # On ajoute la durée
        self.sec += other
        # Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        # On renvoie self
        return self

    """
    >>> from conteneur_02 import Duree
    >>> d = Duree(3,58)
    >>> d += 128
    >>> print(d)
    06:06
    """
