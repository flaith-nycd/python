def mon_decorateur(fonction):
    """ Premier exemple de décorateur """
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction


@mon_decorateur
def salut():
    """ Fonction modifiée par notre décorateur """
    print("Salut !")
