class Robot: 
    # Class attribute shared by all robots
    population = 0

    @classmethod
    def get_population(cls):
        return f"Factory total: {cls.population} robots."

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def transmit_data(self, target):
        # We access the name attribute directly from the target object
        return f"{self.name} sent a data packet to {target.name}."

    def say_hello(self):
        return f"Beep boop, I am {self.name}"

class Drone(Robot): 
    def __init__(self, name, propeller_count):
        # super() runs the parent's setup first
        super().__init__(name)
        self.propeller_count = propeller_count

    def fly(self):
        return f"Whoosh! My {self.propeller_count} propellers are spinning."
    
# --- Building our objects ---
my_robot = Robot("R2-D2") 
my_drone = Drone("Hoverbot", 4)

# --- Testing the interaction ---
print(my_robot.transmit_data(my_drone))

print(Robot.get_population())