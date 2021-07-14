def gen(n):
    yield 1
    yield 10
    yield 100
    yield 1000
    yield 10000


g = gen(100000)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
