from functools import wraps


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("Function {0} was called {1} times.".format(fn.__name__, count))
        return fn(*args, *kwargs)
    inner = wraps(fn)(inner)
    return inner


def add(a, b=0):
    """
    :param a: int
    :param b: int
    :return: a + b
    """
    return a + b


print(help(add))
add = counter(add)
print(help(add))