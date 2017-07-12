"""
Les générateurs sont avant tout un moyen plus pratique de créer et manipuler des itérateurs. 

Quand on demande le premier élément du parcours (grâce à next), la fonction commence son exécution. 
Dès qu'elle rencontre une instruction yield, elle renvoie la valeur qui suit et se met en pause. 
Quand on demande l'élément suivant de l'objet (grâce, une nouvelle fois, à next), 
l'exécution reprend à l'endroit où elle s'était arrêtée et s'interrompt au yield suivant… et ainsi de suite. 
À la fin de l'exécution de la fonction, l'exception StopIteration est automatiquement levée par Python.
"""


def mon_generateur():
    """Notre premier générateur. Il va simplement renvoyer 1, 2 et 3"""
    yield 1
    yield 2
    yield 3


print(mon_generateur)
# <function mon_generateur at 0x00B494F8>
print(mon_generateur())
# <generator object mon_generateur at 0x00B9DC88>
mon_iterateur = iter(mon_generateur())
print(next(mon_iterateur))
# 1
print(next(mon_iterateur))
# 2
print(next(mon_iterateur))
# 3

print("""next(mon_iterateur))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration""")

"""
Quand on l'exécute, on se retrouve avec un générateur. 
Ce générateur est un objet créé par Python qui définit sa propre méthode spéciale __iter__ et donc son propre itérateur.
Nous aurions tout aussi bien pu faire :
"""
for nombre in mon_generateur():  # Attention on exécute la fonction
    print(nombre)
# Notez qu'on doit exécuter la fonction mon_generateur pour obtenir un générateur.
# Si vous essayez de parcourir notre fonction (for nombre in mon_generateur), cela ne marchera pas.

print("----------------")


def intervalle(borne_mini, borne_maxi):
    borne_mini += 1
    while borne_mini < borne_maxi:
        yield borne_mini
        borne_mini += 1

borne = intervalle(5, 20)
for x in borne:
    print(x)