# Class method - bound to the class and not the instance
# - gets class as the first argument
# - a common use is to use as a factory for new instance to be created in
# a different way

# Static method - bound to the class and not the instance
# - does not get any special argument for its first parameter
# -  a common use is to use as a utility function

class Car:

    def __init__(self, color, make, model, door):
        self.color = color
        self.make = make
        self.model = model
        self.door = door
    
    @classmethod
    def with_full_name(cls, color, full_name, door):
        make = full_name.split()[0]
        model = full_name.split()[1]
        return cls(color, make, model, door)
    
    # @classmethod
    # def check_door_for_Uber(cls, door):
    #     if door == 4:
    #         print("Yes")
    #     else:
    #         print("No")
    
    @staticmethod
    def can_be_used_for_Uber(door):
        if door == 4:
            print("Yes")
        else:
            print("No")
    
    def __str__(self):
        return f"This is a {self.color} {self.make} {self.model}"
    

car1 = Car("white", "Toyota", "Corolla", 4)
print(car1)

car2 = Car.with_full_name("black", "Honda Accord", 4)
print(car2)

Car.can_be_used_for_Uber(4)
Car.can_be_used_for_Uber(2)