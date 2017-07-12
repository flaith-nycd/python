class ClassMain:
    def __init__(self):
        print('Dans C')

    def set_x(self, x):
        self.x = x

    def __str__(self):
        # return str(self.x)
        return 'x = {}'.format(str(self.x))

inst = ClassMain()
inst.set_x(30)
print(inst)
