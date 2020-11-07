#memoization Decorator
def fib1(n):
    print('Calculation fib({0})'.format(n))
    return 1 if n < 3 else fib1(n-1) + fib1(n-2)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculation fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


f = Fib()
print(f.fib(10))


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print('Calculation fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

f = fib()

print(f(10))