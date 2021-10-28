# Magic methods
# Also see repr.py

a = 1
print(str(a))
print(repr(a))
print(type(repr(a)))

class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer

    def __str__(self):
        return f"Customized Integer: {self.integer}"

    def __repr__(self):
        return f"Customized Integer({self.integer})"

int1 = CustomizedInteger(4)
print(int1)

print(str(int1))
print(repr(int1))
