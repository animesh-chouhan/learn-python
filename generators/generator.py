# https://www.youtube.com/watch?v=2eiFCQ-YAf4

def gen(n):
    for i in range(n):
        yield i**2


g = gen(100000)

# for i in g:
#     print(i)

# # OR

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

print(next(g))
print(next(g))
print(next(g))
print(next(g))
