"""
class ErreurAnalyseFichier herite de la classe Exception
l'exception ErreurAnalyseFichier hérite de Exception, qui hérite elle-même de BaseException
"""


class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.

    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""

    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message

    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne,
                                    self.message)


raise ErreurAnalyseFichier('file.txt', 30, 'Syntax error')
