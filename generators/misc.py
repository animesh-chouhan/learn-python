import sys


def gen(n):
    for i in range(n):
        yield i**2


g = gen(10000)
x = [i**2 for i in range(10000)]

print(sys.getsizeof(g))
print(sys.getsizeof(x))
