# Class, Attributes and Parameters

class Item:
    # Methods
    def total_price(self):
        return self.price * self.quantity

item1 = Item()

# Assigning attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 2

print(item1.name)
print(type(item1))
print(item1.total_price())

