class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.nom, self.prenom, self.age)

    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)

    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""

        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""

        object.__setattr__(self, nom_attr, val_attr)

"""
>>> from conteneur_00 import Personne
>>> p = Personne('Doe','John')
>>> p
Personne: nom(Doe), prénom(John), âge(33)
>>> print(p)
John Doe, âgé de 33 ans
>>> p.age
33
>>> p.ville
Alerte ! Il n'y a pas d'attribut ville ici !

ma_liste = [1, 2, 3, 4, 5]
8 in ma_liste # Revient au même que ...
ma_liste.__contains__(8)
"""