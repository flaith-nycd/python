"""
    **************************************
    **  Créer une classe dynamiquement  **
    **************************************
"""
""" 
1. On commence par créer deux fonctions, creer_personne et presenter_personne.
   Elles sont amenées à devenir les méthodes __init__ et presenter de notre future classe.
   Étant de futures méthodes d'instance, elles doivent prendre en premier paramètre l'objet manipulé.
"""


def creer_personne(personne, nom, prenom):
    """La fonction qui jouera le rôle de constructeur pour notre classe Personne.

    Elle prend en paramètre, outre la personne :
    nom -- son nom
    prenom -- son prenom"""

    personne.nom = nom
    personne.prenom = prenom
    personne.age = 21
    personne.lieu_residence = "Lyon"


def presenter_personne(personne):
    """Fonction présentant la personne.

    Elle affiche son prénom et son nom"""

    print("{} {}".format(personne.prenom, personne.nom))


"""
2. On place ces deux fonctions dans un dictionnaire. En clé se trouve le nom de la future méthode et en valeur, 
   la fonction correspondante.
"""
# Dictionnaire des méthodes
methodes = {
    "__init__": creer_personne,
    "presenter": presenter_personne,
}

"""
3. Enfin, on fait appel à type en lui passant, en troisième paramètre, le dictionnaire que l'on vient de constituer.
"""
# Création dynamique de la classe
Personne = type("Personne", (), methodes)

# >>> john = Personne("Doe", "John")
john = Personne("Doe", "John")

# >>> john.nom
# 'Doe'
print(john.nom)

# >>> john.prenom
# 'John'
print(john.prenom)

# >>> john.age
# 21
print(john.age)

# >>> john.presenter()
# John Doe
john.presenter()
