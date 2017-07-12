class StaticTest:
    nb_instance = 0

    def __init__(self):
        self.count()

    @classmethod
    def count(cls):
        cls.nb_instance += 1

    @classmethod
    def num_instance(cls):
        return cls.nb_instance


class StaticTestChild(StaticTest):
    nb_instance = 0


# Create few instances
StaticTest()
StaticTest()
StaticTest()

print(StaticTest.num_instance())

# How many instances from our child class?
print(StaticTestChild.num_instance())
