# Static methods don't take any arguments by default
# Normal methods: self
# Class methods: cls

class Item:

    all = []

    def __init__(self, name: str, price: float, quantity: int):

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @staticmethod
    def is_integer(num):
        return isinstance(num, int)


    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}))"


print(Item.is_integer( 2.0))

