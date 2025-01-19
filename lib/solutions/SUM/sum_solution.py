# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):
    if x and y:
        if x > 0 and y > 0:
            return x + y
    else:
        raise Exception
