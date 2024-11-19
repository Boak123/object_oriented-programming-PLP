# Create a class representing anything you like (a Smartphone, Book, Animal, etc.)
class Smartphone:
    # attributes: brand, model, price, color, memory
    color = "Black"
    memory = "64GB"
    def __init__(self, brand, model, price, color, memory):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.memory = memory

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
        print(f"Color: {self.color}")
        print(f"Memory: {self.memory}")

    def change_price(self, new_price):
        self.price = new_price

    def change_color(self, new_color):
        self.color = new_color

#object
smartphone1 = Smartphone("Samsung", "Galaxy S10", 500, "Blue", "128GB")
smartphone1.display_info()
smartphone1.change_price(600)
smartphone1.change_color("Red")
smartphone2 = Smartphone("Apple", "iPhone 11", 700, "White", "256GB")
smartphone2.display_info()
smartphone2.change_price(800)