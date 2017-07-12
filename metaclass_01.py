class Personne:
    """Classe définissant une personne.

    Elle possède comme attributs :
    nom -- le nom de la personne
    prenom -- son prénom
    age -- son âge
    lieu_residence -- son lieu de résidence

    Le nom et le prénom doivent être passés au constructeur."""

    # la méthode __new__, appelée pour créer une classe
    def __new__(cls, nom, prenom):
        print("Appel de la méthode __new__ de la classe {}".format(cls))

        # On laisse le travail à object
        '''
            A partir de la version 3.3, on ne passe plus de parametres
            return object.__new__(cls, nom, prenom)
        '''
        return object.__new__(cls)

    # la méthode __init__, appelée pour construire la classe
    def __init__(self, nom, prenom):
        """Constructeur de notre personne."""
        print("Appel de la méthode __init__")
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_residence = "Lyon"


personne = Personne("Doe", "John")

