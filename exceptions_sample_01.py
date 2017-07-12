def f(a, b):
    try:
        x = a / b
    except ZeroDivisionError as exceptError:
        print('Division by zero error !')
        print(exceptError.args)
    except TypeError:
        print('Unsuported operand ({}, {}), only integer allowed !'.format(a, b))
    else:
        print('Result of {} / {} = {}'.format(a, b, x))
    finally:
        print("Let's continue...")
    print('again :)')
    print()

f(0, 2)
f(1, 2)
f(1, 0)
f(1, 'a')
