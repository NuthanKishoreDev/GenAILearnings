#Enterprise Order Processing System
#Description: This module assists in processing customer orders by validating order details, checking inventory levels, and processing payments.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)

laptop = Product("Laptop", 90000)
mouse = Product("Mouse", 2000)

order = Order()
order.add_item(laptop, 3)
order.add_item(mouse, 3)

print("Total Order Value:", order.total())
# output: Total Order Value: 276000
#explanation: laptop price 90000 * 3 = 270000 + mouse price 2000 * 3 = 6000; Total = 276000
# This code demonstrates basic order processing by adding products to an order and calculating the total value.
print("-----")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price
        
user = User("Nuthan","nuthan@ww.com")
product = Product("Laptop", 90000)

print(f"User {user.username} with email {user.email} is interested in product {product.name} priced at {product.price}.")
