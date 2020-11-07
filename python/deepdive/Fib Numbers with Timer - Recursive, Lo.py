# Fib Numbers with Timer - Recursive, Loop, Reduce.
def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0} {1} took {2:.6f} seconds to run'.format(fn.__name__,
                                                          args_str,
                                                          elapsed))
        return result

    return inner


def calc_recursive_fib(n):
    """
    recursion
    """
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


@timed
def fib_recursive(n):
    return calc_recursive_fib(n)


print(fib_recursive(6))


@timed
def fib_loop(n):
    """
    Loop
    """
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(6))


from functools import reduce

@timed
def fib_reduce(x):
    initial = (1,0)
    dummy = range(x)
    fib_n = reduce(lambda prev, x: (prev[0]+ prev[1], prev[0]),
                                    dummy,
                                    initial)
    return fib_n[0]


print(fib_reduce(35))

