class StaticTest:
    nb_instance = 0

    def __init__(self):
        StaticTest.nb_instance += 1

    def num_instance():
        return StaticTest.nb_instance

    # Generate our method as a static method
    num_instance = staticmethod(num_instance)


class StaticTestChild(StaticTest):
    def num_instance():
        return 'Static Test Child Number of Instance: {}'.format(StaticTest.nb_instance)

    # Generate our method as a static method again
    num_instance = staticmethod(num_instance)


# Displayt how many instance have been created
print(StaticTest.num_instance())

# Create few instances
StaticTest()
StaticTest()
StaticTest()

# How many instances from our child class?
print(StaticTestChild.num_instance())
