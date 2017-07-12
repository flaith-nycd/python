# Check: http://www.diveintopython3.net/iterators.html
class Mots01:
    def __init__(self, phrase):
        self.list_mots = phrase.split()
        self.count = 0

    # To be sure that each time we call a for function, for example, like [x for x in m]
    # it will give us each value
    def __iter__(self):
        # Return self will only return it once
        return self

    # next resumes where it left off
    def __next__(self):
        if self.count == len(self.list_mots):
            raise StopIteration
        self.count = self.count + 1
        return self.list_mots[self.count - 1]


print('Version 1')
m = Mots01('spam egg beans spam knight')
a = [x for x in m]
b = [x for x in m]

print(a)
# Result: ['spam', 'egg', 'beans', 'spam', 'knight']
print(b)
# Result: []


class Mots02:
    def __init__(self, phrase):
        self.list_mots = phrase.split()

    def __iter__(self):
        # Call another class to keep the iteration
        return IterMots(self.list_mots)


class IterMots:
    def __init__(self, phrase):
        self.list_mots = phrase
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.list_mots):
            raise StopIteration
        self.count = self.count + 1
        return self.list_mots[self.count - 1]


print();
print('Version 2')
m = Mots02('spam egg beans spam knight')
a = [x for x in m]
b = [x for x in m]

print(a)
# Result: ['spam', 'egg', 'beans', 'spam', 'knight']
print(b)
# Result: ['spam', 'egg', 'beans', 'spam', 'knight']


class Mots03:
    def __init__(self, phrase):
        self.list_mots = phrase.split()

    def __iter__(self):
        # Use generator
        for mot in self.list_mots:
            # "yield" pauses a function
            # Genere/produit
            yield mot


m = Mots03('spam egg beans spam knight')
a = [x for x in m]
b = [x for x in m]

print(); print('Version 3')
print(a)
# Result: ['spam', 'egg', 'beans', 'spam', 'knight']
print(b)
# Result: ['spam', 'egg', 'beans', 'spam', 'knight']
