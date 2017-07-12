def gen(x):
    for i in range(x):
        # "yield" pauses a function
        # Genere/produit
        yield i ** 3 - 3 * i + 2

tt = [i for i in gen(100) if i % 17 == 0]

print(tt)
