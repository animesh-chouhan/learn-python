# https://betterprogramming.pub/exploring-map-vs-starmap-in-python-6bcf32f5fa4a#:~:text=map()%20%3A%20Multiple%20iterables%20are,and%20starmap%20object%20are%20iterators.

# map(function, iterable, ...)
# Return an iterator that applies function to every item of 
# iterable, yielding the results. If additional iterable arguments 
# are passed, function must take that many arguments and 
# is applied to the items from all iterables in parallel. 
# With multiple iterables, the iterator stops when the shortest 
# iterable is exhausted. For cases where the function inputs are 
# already arranged into argument tuples, see itertools.starmap().

# return type is a map object which is iterable

def square(x):
    return x * x

nums = [1, 2, 3, 4]
out1 = map(square, nums)
print(out1)

# Accessing the map object:
# 1.Using the list() or tuple() constructor
print(list(out1))
# 2.Using for loop
# Either listing or for-looping
# will exhaust the iterator.  This is how iterators work.
# for num in out1:
#     print(num)
out2 = map(square, nums)
for num in out2:
    print(num)

# 3.Accessing the next element using next() function
out3 = map(square, nums)
print(next(out3))
print(next(out3))
print(next(out3))
print(next(out3))
# print(next(out3)) Iterable exhausted

# Applying a function to more iterables
def mult(x, y, z):
    return x * y * z

num1=[1,2,3,4]
num2=[2,4,6,8]
num3=[2,3,4,5]
s=map(mult,num1,num2,num3)
print (list(s))