class try_decorator(object):
    def _decorator(foo):
        def magic(self):
            print("start magic")
            foo(self)
            print("end magic")

        return magic

    @_decorator
    def bar(self):
        print("normal call")


test = try_decorator()

test.bar()


class TestA(object):
    def _decorator(foo):
        def magic(self):
            print("start magic")
            foo(self)
            print("end magic")

        return magic

    @_decorator
    def bar(self):
        print("normal call")

    _decorator = staticmethod(_decorator)


class TestB(TestA):
    @TestA._decorator
    def bar(self):
        print("override bar in")
        super(TestB, self).bar()
        print("override bar out")


print("Normal:")
test = TestA()
test.bar()
print()

print("Inherited:")
b = TestB()
b.bar()
print()
