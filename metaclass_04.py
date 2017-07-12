#!/usr/bin/env python3
"""
    *********************************
    **  Les métaclasses en action  **
    *********************************
"""

"""
Par exemple, dans une bibliothèque destinée à construire des interfaces graphiques, 
on trouve plusieurs widgets (ce sont des objets graphiques) comme des boutons, des cases à cocher, des menus, 
des cadres...

Généralement, ces objets sont des classes héritant d'une classe mère commune. 
En outre, l'utilisateur peut, en cas de besoin, créer ses propres classes héritant des classes de la bibliothèque.

Par exemple, la classe mère de tous nos widgets s'appellera Widget. De cette classe hériteront les classes Bouton, 
CaseACocher, Menu, Cadre, etc. L'utilisateur de la bibliothèque pourra par ailleurs en dériver ses propres classes.

Le dictionnaire que l'on aimerait créer se présente comme suit :

{
    "Widget": Widget,
    "Bouton": Bouton,
    "CaseACocher": CaseACocher,
    "Menu": Menu,
    "Cadre": Cadre,
    ...
}

Ce dictionnaire pourrait être rempli manuellement à chaque fois qu'on crée une classe héritant de Widget mais 
avouez que ce ne serait pas très pratique.
"""

trace_classes = {}  # Notre dictionnaire vide


class MetaWidget(type):
    """Notre métaclasse pour nos Widgets.

    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera créée, utilisant cette métaclasse naturellement."""

    def __init__(cls, nom, bases, dict):
        """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls


# Créons notre classe Widget :
class Widget(metaclass=MetaWidget):
    """Classe mère de tous nos widgets."""
    pass


# Après avoir exécuté ce code, vous pouvez voir que notre classe Widget a bien été ajoutée dans notre dictionnaire :
# >>> trace_classes
# {'Widget': <class '__main__.Widget'>}
# >>>
print(trace_classes)


# Maintenant, construisons une nouvelle classe héritant de Widget.
class Bouton(Widget):
    """Une classe définissant le widget bouton."""
    pass


print(trace_classes)

"""

    En résumé

    * Le processus d'instanciation d'un objet est assuré par deux méthodes, __new__ et __init__.
    * __new__ est chargée de la création de l'objet et prend en premier paramètre sa classe.
    * __init__ est chargée de l'initialisation des attributs de l'objet et prend en premier paramètre 
      l'objet précédemment créé par __new__.
    * Les classes étant des objets, elles sont toutes modelées sur une classe appelée métaclasse.
    * À moins d'être explicitement modifiée, la métaclasse de toutes les classes est type.
    * On peut utiliser type pour créer des classes dynamiquement.
    * On peut faire hériter une classe de type pour créer une nouvelle métaclasse.
    * Dans le corps d'une classe, pour spécifier sa métaclasse, on exploite la syntaxe suivante:
      class MaClasse(metaclass=NomDeLaMetaClasse):

"""
