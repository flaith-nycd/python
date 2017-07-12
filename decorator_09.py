# Multiple decorators
def b(fn):
    return lambda s: '<b>%s</b>' % fn(s)


def em(fn):
    return lambda s: '<em>%s</em>' % fn(s)


@b
@em
def greet(name):
    return 'Hello, %s!' % name


print(greet('world'))


# Decorators with arguments
def tag_wrap(tag):
    def decorator(fn):
        def inner(s):
            # return '<%s>%s' % (fn(s), tag)
            return '<%s>%s</%s>' % (tag, fn(s), tag)

        return inner

    return decorator


@tag_wrap('b')
@tag_wrap('em')
def greet(name):
    return 'Hello, %s!' % name


print(greet('world'))
