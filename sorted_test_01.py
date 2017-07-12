# https://wiki.python.org/moin/HowTo/Sorting
# https://docs.python.org/3.6/howto/sorting.html#sortinghowto
# https://developers.google.com/edu/python/sorting
from operator import itemgetter
from operator import attrgetter

# Using itemgetter from operator
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

sorted_etudiant_second_column = sorted(etudiants, key=itemgetter(2))
print(sorted_etudiant_second_column)


# Using attrgetter from operator
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr(('Student: {}, Grade: {}, age: {}'.format(self.name.capitalize(), self.grade, self.age)))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=attrgetter('age')))  # sort by age
print(sorted(student_objects, key=attrgetter('age'), reverse=True))  # sort by age descending


# Multiple criteria
class LigneInventaire:
    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{})>".format(
            self.produit, self.prix, self.quantite)


# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

print(sorted(inventaire, key=attrgetter("prix", "quantite")))
