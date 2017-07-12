def singleton(classe_definie):
    instances = {}  # Dictionnaire de nos instances singletons

    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]

    return get_instance


@singleton
def single_function_called():
    pass


a = single_function_called()
b = single_function_called()
if a is b:
    print(hex(id(a)))
    print(hex(id(b)))
    print('Class "a" is Class "b"')


# From https://www.python.org/dev/peps/pep-0318/#examples
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    pass

a = MyClass()
b = MyClass()
if a is b:
    print(hex(id(a)))
    print(hex(id(b)))
    print('Class "a" is Class "b"')
