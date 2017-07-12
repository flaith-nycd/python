class ContextManager:
    def __enter__(self):
        print('Inside __enter__')
        # Always have to return the instance of the object
        return self

    # *args will give us a tuple or arguments
    def __exit__(self, *args):
        print('Inside __exit__')
        # If there is an exception, we display it
        if args[0] is not None:
            print('Arguments: ')
            for arg in args:
                print('---> ', arg)
        # Always have to return 'True' or 'False'
        # If an exception occurs, we will keep it with 'True'
        # If 'False' we will return the exception
        # return False
        return True

    # For a test
    def divide(self, a, b):
        print('Div {}/{} = {}'.format(a, b, a / b))


# Context Manager test
with ContextManager() as cm:
    cm.divide(5, 0)
