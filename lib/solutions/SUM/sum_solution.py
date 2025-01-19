# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x and y:
        if x > 0 and y > 0:
            return x + y
        else:
            raise Exception