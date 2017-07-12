# https://www.python.org/dev/peps/pep-0318/
# Decorating with parameters


def works_for_all(func):
    def inner(*args, **kwargs):
        if args:
            print("I can decorate any function with the following parameters:")
            for one_arg in args:
                print('      arg: "', one_arg, '"', sep='')
        if kwargs:
            for one_arg in kwargs:
                print('   kwargs: "', one_arg, '" = "', kwargs[one_arg], '"', sep='')
        return func(*args, **kwargs)

    return inner


@works_for_all
def do_someting(*a, **b):
    if a and b:
        print('Do something with:')
        print('    *a =', a)
        print('   **b =', b)
    else:
        print('Do nothing...')


do_someting('test param1', volume=4, toto='titi')
print()
do_someting()


def mon_decorateur(fonction):
    """Premier exemple de décorateur"""
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction


@mon_decorateur
def salut():
    """Fonction modifiée par notre décorateur"""
    print("Salut !")


salut()
