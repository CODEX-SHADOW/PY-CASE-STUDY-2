class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_quantity(self, quantity):
        self.quantity += quantity

    def update_price(self, price):
        self.price = price

    def sell(self, quantity):
        if self.quantity < quantity:
            raise Exception("Out of stock")
        self.quantity -= quantity

    def __str__(self):
        return f"{self.name} - {self.quantity} x {self.price} = {self.quantity * self.price}"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def update_product(self, product, new_product):
        index = self.products.index(product)
        self.products[index] = new_product

    def sell_product(self, product_name, quantity):
        product = self.get_product(product_name)
        product.sell(quantity)

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        raise Exception("Product not found")

    def __str__(self):
        return "\n".join([str(product) for product in self.products])


def main():
    store = Store()

    # Add products to the store
    product1 = Product("Product 1", 10, 100)
    product2 = Product("Product 2", 20, 50)
    store.add_product(product1)
    store.add_product(product2)

    # Sell a product
    try:
        store.sell_product("Product 1", 5)
    except Exception as e:
        print(e)

    # Get the total value of inventory
    total_value = 0
    for product in store.products:
        total_value += product.quantity * product.price

    print("Total value of inventory:", total_value)


if __name__ == "__main__":
    main()
