def check_if_less(value):
    if value < 0:
        return True
    else:
        return False


def apply_when_less(value):
    return -1


def check_if_equal(value):
    if value == 0:
        return True
    else:
        return False


def apply_when_equal(value):
    return 0


def check_if_greater(value):
    if value > 0:
        return True
    else:
        return False


def apply_when_greater(value):
    return 1


rules = ((check_if_less, apply_when_less),
         (check_if_equal, apply_when_equal),
         (check_if_greater, apply_when_greater)
         )


def check_and_apply(value):
    for check_rule, apply_rule in rules:
        if check_rule(value):
            return apply_rule(value)

print(check_and_apply(-10))
print(check_and_apply(0))
print(check_and_apply(10))
