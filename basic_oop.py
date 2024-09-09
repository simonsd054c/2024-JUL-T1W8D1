# Classes - are blueprints for creating objects/instances
# naming conventions
# classes - PascalCase

# Car has attributes - color, make, model
class Car:
    # Constructor
    def __init__(self, _color, make, model):
        self._color = _color
        self.make = make
        self.model = model
        self.engine = None
    
    # getters or accessors
    def get_color(self):
        # do if checks
        return self._color
    
    # setters or mutators
    def set_color(self, color):
        # do some if checks
        self._color = color
        # do some side-effects
    
    def run(self):
        print(f"{self.make} {self.model} is running!!! Vrrrooooommm Vrrrooooommm!!!")
    
    def attach_engine(self, engine):
        self.engine = engine
    
    def __str__(self):
        return f"This is a {self._color} {self.make} {self.model}"

# Inheritance - is-a relationship
# Petrol Car is a Car
class PetrolCar(Car):
    def __init__(self, _color, make, model, capacity_of_tank):
        super().__init__(_color, make, model)
        self.capacity_of_tank = capacity_of_tank

# Electric Car is a Car
class ElectricCar(Car):
    
    # Function Overriding
    def run(self):
        print("I do not make noise. I run silently. No Vrooming!!")
    
    # Function Overloading - Not supported in python
    # def run(self, distance):
    #     print(f"I will run {distance}km")

# Composition - has-a relationship
class Engine:
    def __init__(self, power):
        self.power = power
    
    def __str__(self):
        return f"This engine has a power of {self.power}"

my_car = Car("White", "Honda", "Civic")
my_car.run()
print(my_car)
my_car.set_color("Yellow")
print(my_car.get_color())

your_car = Car("Grey", "Toyota", "Camry")
your_car.run()
print(your_car)


petrol_car1 = PetrolCar("Blue", "Mazda", "CX5", 40)
petrol_car1.run()
print(petrol_car1.capacity_of_tank)

electric_car1 = ElectricCar("White", "Tesla", "3")
electric_car1.run()
# electric_car1.run(12)

engine1 = Engine("200hp")

engine2 = Engine("220hp")

my_car.attach_engine(engine2)
print(my_car.engine)

your_car.attach_engine(engine1)