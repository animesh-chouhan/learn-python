# https://betterprogramming.pub/exploring-map-vs-starmap-in-python-6bcf32f5fa4a#:~:text=map()%20%3A%20Multiple%20iterables%20are,and%20starmap%20object%20are%20iterators.

# itertools.starmap(function, iterable)
# Make an iterator that computes the function using arguments 
# obtained from the iterable. Used instead of map() when argument 
# parameters are already grouped in tuples from a single iterable 
# (the data has been “pre-zipped”). 

# The difference between map() and starmap() parallels the 
# distinction between function(a,b) and function(*c).
# — Python’s documentation https://docs.python.org/3/library/itertools.html#itertools.starmap

# Items inside the iterable should also be iterable. Otherwise, 
# it will raise a TypeError.
# The return type is an itertools.starmap object which is an iterator

from itertools import starmap

def mult(x, y):
    return x * y

nums = [(1, 2), (2, 3)]
out1 = starmap(mult, nums)
print(list(out1))

# Applying a lambda function
out2 = starmap((lambda x, y: x + y), nums)
print(list(out2))

# Conclusion
# 1.map(): Multiple iterables are allowed.
# 2.starmap(): Only one iterable is allowed. Items inside the iterable should also be iterable.
# 3.Both the map object and starmap object are iterators.
# 4.map(): Built-in function.
# 5.itertools.starmap(): You have to import the itertools module.