number = 500
liste_origine = [x for x in range(2, number)]
prime_number = [nbp for nbp in liste_origine if all(nbp % y != 0 for y in range(2, nbp))]
print(prime_number)
