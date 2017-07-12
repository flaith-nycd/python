"""
Contrôler les types passés à notre fonction
"""
# https://www.python.org/dev/peps/pep-0318/


def controler_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""

        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""

            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                # if not isinstance(a_args[i], type(args[i])):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(i, a_args[i]))

            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type précisé".format(repr(cle)))
                # if not isinstance(a_kwargs[cle], type(kwargs[cle])):
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type {1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)

        return fonction_modifiee

    return decorateur


@controler_types(int, int)
def intervalle(base_inf, base_sup):
    print("Intervalle de {0} à {1}".format(base_inf, base_sup))


intervalle(1, 8)
# Intervalle de 1 à 8

intervalle(5, "oups!")
# Traceback (most recent call last):
#   File "E:/Projects/apple/Sherwood Forest/Sherwood disasm/decorator_08.py", line 51, in <module>
#     intervalle(5, "oups!")
#   File "E:/Projects/apple/Sherwood Forest/Sherwood disasm/decorator_08.py", line 27, in fonction_modifiee
#     raise TypeError("l'argument {0} n'est pas du type {1}".format(i, a_args[i]))
# TypeError: l'argument 1 n'est pas du type <class 'int'>
