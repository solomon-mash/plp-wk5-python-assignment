class Transport:
    def move(self):   # initial implentation of move function
        print("The Object is moving")
class Car(Transport):
    def move(self): # Different implementation of inherited function move
        print("The car is driving on the road.")

class Plane(Transport): # Different implementation of inherited function move
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Transport):
    def move(self):   # Different implementation of inherited function move
        print("The boat is sailing on the water.")

class Bicycle(Transport):
    def id(self):
        print("Bicycle tracking id is ix56895")

# Create instances
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

car.move()
plane.move()
boat.move()
bicycle.id()
bicycle.move()  # Unmodified inherited move() method

