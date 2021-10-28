class Item:
    # Class attribute
    pay_rate = 0.8
    
    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} isn't greater than zero"
        assert quantity >= 0


        #Assign to self object
        print(f"Instance Created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity


    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # or Item.pay_rate

item1 = Item("Phone", 100, 5)

print(item1.name)
print(item1.total_price())

# Accessing class attribute
print(Item.pay_rate)
print(item1.pay_rate)

# All the attributes 
# print(Item.__dict__)
# print(item1.__dict__)

item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)