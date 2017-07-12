class Foo:
    def bar1(self):
        print(1)

    def bar2(self):
        print(2)


def callMethod(o, name):
    getattr(o, name)()


f = Foo()
callMethod(f, "bar1")
