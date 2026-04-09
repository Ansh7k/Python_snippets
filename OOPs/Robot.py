class Robot: # class robot
    def __init__(self, name):
        self.name = name

    def transmit_data(self, target):
        return f"{self.name} send a data packet to {target.name}"

    def say_hello(self):
        return f"Beep boop, I am {self.name}"

my_robot = Robot("R2-D2") # instance of class robot
print(my_robot.say_hello()) # instance calling the method of original class


class Drone(Robot): #inherit class 
    def __init__(self, name, propeller_count):
        super().__init__(name)
        self.propeller_count = propeller_count

    def fly(self):
        return f"Whoosh! My {self.propeller_count} are spinning."
    
my_drone = Drone("Hoverbot", 4)

print(my_drone.say_hello())
print(my_drone.fly())

print(my_robot.transmit_data(my_drone))