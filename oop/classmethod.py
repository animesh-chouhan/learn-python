# Classmethods are used as alternative constructors
import csv


class Item:

    all = []

    def __init__(self, name: str, price: float, quantity: int):

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instanstiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                print(item)
                name = item["name"]
                price = int(item["price"])
                quantity = int(item["quantity"])
                cls(name, price, quantity)

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}))"


Item.instanstiate_from_csv()

print(Item.all)

for instance in Item.all:
    print(instance.name)

