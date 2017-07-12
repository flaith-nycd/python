class StaticTest:
    nb_instance = 0

    def __init__(self):
        StaticTest.nb_instance += 1

    @staticmethod
    def num_instance():
        return StaticTest.nb_instance


class StaticTestChild(StaticTest):
    @staticmethod
    def num_instance():
        return 'Static Test Child Number of Instance: {}'.format(StaticTest.nb_instance)


# Displayt how many instance have been created
print(StaticTest.num_instance())

# Create few instances
StaticTest()
StaticTest()
StaticTest()

# How many instances from our child class?
print(StaticTestChild.num_instance())
