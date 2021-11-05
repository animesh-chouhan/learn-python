# Parent Class
class Item:
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} isn't greater than zero"
        assert quantity >= 0


        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}))"

# Child Class
class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        # Call to super function
        super().__init__(name, price, quantity)
        
        assert quantity >= 0

        self.broken_phones = broken_phones


phone1 = Phone("Pixel", 500, 5, 1)
print(phone1.broken_phones)

phone2 = Phone("Samsung", 700, 5, 1)