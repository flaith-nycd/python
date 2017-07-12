class StaticTest:
    nb_instance = 0

    def __init__(self):
        StaticTest.nb_instance += 1

    def num_instance():
        return StaticTest.nb_instance

    # Generate our method as a static method
    num_instance = staticmethod(num_instance)

# Displayt how many instance have been created
print(StaticTest.num_instance())

# Create a new instance
StaticTest()

# How many?
print(StaticTest.num_instance())

# Create another instance
sm = StaticTest()

print(sm.num_instance())
