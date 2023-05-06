class Fruit:

    quantity = 0

    def __init__(self,name, price, color ):
        self.fruit_name = name
        self.fruit_price = price
        self.fruit_color = color

    def add_fruits(self, quant):
        self.quantity+=quant
        return f"There are now {self.quantity} {self.fruit_name}"
    
    def remove_fruits(self, quant):
        self.quantity-=quant
        return f"There are now {self.quantity} {self.fruit_name}"
    
    def eat_fruit(self):
        return f"Here's a {self.fruit_name}, enjoy!"
    

fruit1 = Fruit("Watermelon", "Ksh.400", "Green")
fruit2 = Fruit("Banana", "Ksh.10", "Yellow")

print(fruit1.add_fruits(10))
print(fruit1.remove_fruits(2))
print(fruit1.eat_fruit())

print(fruit2.add_fruits(100))
print(fruit2.remove_fruits(20))
print(fruit2.eat_fruit())


