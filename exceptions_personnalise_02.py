class SplitError(Exception):
    def __init__(self, res, val):
        self.res = res
        self.val = val


try:
    raise SplitError(res='qwerty', val=98)
except SplitError as e:
    print(e.res)
    print(e.val)
