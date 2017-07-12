"""
Pour l'heritage multiple, il suffit de faire:
class MaClasseHeritee(MaClasseMere1, MaClasseMere2):
La recherche des classes meres se fait a partir de la premiere classe (de la gauche vers la droite)
ici: MaClasseMere1 en permier
"""


class Personne:
    """Classe représentant une personne"""

    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)


class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""

    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

agent = AgentSpecial("Fisher", "18327-121")
print(agent.nom)
# 'Fisher'
print(agent)
# Agent Fisher, matricule 18327-121
print(agent.prenom)
# 'Martin'
