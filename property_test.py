class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

c = C()
print(c.x)
c.x = 3
print(c.x)
c.delx()
# Cannot call now
# print(c.x)

p = Parrot()
print(p)
# < Parrot object at 0x000000000??????? >
print(p.voltage)
# 100000
