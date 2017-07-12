"""
L'encapsulation est un principe qui consiste à cacher ou protéger certaines données de notre objet. 
Pour y acceder, on utilise des accesseurs et des mutateurs (methodes 'get' et 'set')

On va utiliser ce systeme si l'on doit effectuer des taches repetitives
a chaque fois que l'on souhaite acceder ou modifier une valeur
"""


class Encapsulation():
    def __init__(self, val):
        print("--INIT called")
        # Notez le nom de la variable, il y a un '_' devant
        self._val = val

    # Notez bien le '_' devant le nom de la methode, comme pour la variable ci-dessus
    # c'est une convention, celle-ci veut que l'on n'accède pas, depuis l'extérieur de la classe,
    # à un attribut commençant par '_'
    def _get_value(self):
        # Ici on peut faire appels a d'autres methodes ou faire des tests ...
        print("GET is called")
        return self._val

    def _set_value(self, value):
        # Ici on peut faire appels a d'autres methodes ou faire des tests ...
        print("SET is called with the new value {}".format(value))
        self._val = value

    def __del__(self):
        print("--DEL called")

    # Définition d'une propriété: On lui dit que l'attribut val (sans '_') doit être une propriété.
    # On définit dans notre propriété, dans l'ordre, la méthode d'accès (l'accesseur)
    # et celle de modification (le mutateur).
    # Forme de definition:
    # nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide)
    val = property(_get_value, _set_value)


t = Encapsulation(33)
print(t.val)  # Affiche "GET is called" et la valeur 33
t.val = 88  # Affiche "SET is called with the new value 88"
print(t.val)  # Affiche "GET is called" et la nouvelle valeur 88
