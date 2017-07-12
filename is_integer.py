def isinteger(x):
    try:
        return int(x) == x
    except:
        return False