# PY-CASE-STUDY-2
JUST ANOTHER COLLEGE ASSIGNMENT 
Case Study 2: Inventory Management System
Develop an inventory management system for a small retail store using Python. You need to create classes for products, manage their quantities, and handle sales transactions. Utilize object-oriented programming to define classes for products and implement functions for adding, updating, and selling products. Incorporate exception handling to handle cases like out-of-stock products.
This inventory management system is designed to help a small retail store track its product inventory and handle sales transactions.

Then, you could go into more detail about the different classes and functions in the code. For example:

The Product class represents a product in the inventory system. It has attributes for the product name, price, and quantity. It also has methods for adding and selling products, and updating the product price.
The Store class represents a retail store. It has an attribute for a list of products in the store. It also has methods for adding, removing, and updating products in the store, and selling products to customers.
You could also provide some examples of how to use the code. For example:


Python
# Create a new store
store = Store()

# Add products to the store
product1 = Product("Product 1", 10, 100)
product2 = Product("Product 2", 20, 50)
store.add_product(product1)
store.add_product(product2)

# Sell a product
store.sell_product("Product 1", 5)

# Get the total value of inventory
total_value = 0
for product in store.products:
    total_value += product.quantity * product.price

print("Total value of inventory:", total_value)


Finally, you could include a section on exception handling. For example:

The system uses exception handling to handle cases like out-of-stock products. If a customer tries to sell more of a product than is in stock, the system will raise an Exception and the sale will not be completed.
