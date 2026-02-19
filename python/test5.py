import os
import sys

def calculate_total(price, tax
    total = price + tax
    print("Total is: " total)
    return total

class Order
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

order = Order()
order.add_item("Book")

result = calculate_total("100", 5)
print(result
