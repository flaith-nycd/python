def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
    en fonction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.

    Note: borne_inf doit être inférieure à borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None:  # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
            print('borne_inf: {}'.format(borne_inf))
        borne_inf += 1


generateur = intervalle(10, 25)
for nombre in generateur:
    if nombre == 15:  # On saute à 20
        generateur.send(20)
    # print(nombre, end=" ")
    print(nombre)
