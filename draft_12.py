class Person:
    def __init__(self, name):
        self.person_name = name

    @property
    def name(self):
        return self.person_name


me = Person('Nico')

# With property defined in the class
print(me.name)

# Without property defined
# print(me.name())
