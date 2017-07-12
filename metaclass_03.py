"""
Définition d'une métaclasse

la méthode __new__, appelée pour créer une classe ;
la méthode __init__, appelée pour construire la classe.
"""

"""
    **************************
    **  La méthode __new__  **
    **************************
"""

"""
Elle prend quatre paramètres :

la métaclasse servant de base à la création de notre nouvelle classe ;
le nom de notre nouvelle classe ;
un tuple contenant les classes dont héritent notre classe à créer ;
le dictionnaire des attributs et méthodes de la classe à créer.
Les trois derniers paramètres, vous devriez les reconnaître : ce sont les mêmes que ceux passés à type.

Voici une méthode __new__ minimaliste.
"""


class MaMetaClasse(type):
    """Exemple d'une métaclasse."""

    def __new__(metacls, nom, bases, dict):
        """Création de notre classe."""
        print("On crée la classe {}".format(nom))
        return type.__new__(metacls, nom, bases, dict)


class MaClasse(metaclass=MaMetaClasse):
    pass


# En exécutant ce code, vous pouvez voir :
# >>> On crée la classe MaClasse

"""
    **************************
    **  La méthode __new__  **
    **************************
"""

"""
Le constructeur d'une métaclasse prend les mêmes paramètres que __new__, sauf le premier, 
qui n'est plus la métaclasse servant de modèle mais la classe que l'on vient de créer.

Les trois paramètres suivants restent les mêmes : le nom, le tuple des classes-mères et 
le dictionnaire des attributs et méthodes de classe.

Il n'y a rien de très compliqué dans le procédé, l'exemple ci-dessus peut être repris 
en le modifiant quelque peu pour qu'il s'adapte à la méthode __init__.
"""
