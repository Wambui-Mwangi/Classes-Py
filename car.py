class Car:
    speed = 0

    def __init__(self, make, model, number_plate):
        self.car_make = make
        self.car_model = model
        self.car_number_plate = number_plate

    def car_start(self):
        return "Starting the engine"
    
    def car_accelerate(self, kmh):
        self.speed += kmh
        return f"Accelerating to {self.speed} kmh"
    
    def car_stop(self):
        self.speed = 0
        return "The car is stopping"

car1 = Car("Toyota", "Corolla", "KAK 761V")
car2 = Car("Mercedes", "S-Class", "KDG 345T")

print(car1.car_start())
print(car1.car_accelerate(30))
print(car1.car_stop())

print(car2.car_start())
print(car2.car_accelerate(80))
print(car2.car_stop())