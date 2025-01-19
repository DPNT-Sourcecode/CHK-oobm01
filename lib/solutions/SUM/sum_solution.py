# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x and y:
        if x > -1 and y > -1:
            return x + y
    else:
        raise Exception