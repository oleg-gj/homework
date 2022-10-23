# Task 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print("Speed is increased")

    def breake_speed(self):
        print("Breake")

    def mileage_info(self):
        print(f"Millage: {self.mileage}")

# Task 2

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed,mileage)

    def seating_capacity(self):
        print("Seating capasity: ")

bus = Bus(10, 500)
bus.mileage_info()

# Task 3
print(issubclass(Bus, Vehicle))

# Task 4
school_bus = Bus(120, 300_000)
print(isinstance(school_bus, Bus))
print(isinstance(school_bus, Vehicle))

# Task 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


    def school_address(self):
        print("School address: ")

    def main_subject(self):
        print("Main subject: ")
school = School(1, 15)

# Task 6
class SchoolBus(Bus, School):
    def __init__(self,max_speed, mileage, get_school_id, number_of_students ):
        super().__init__(max_speed, mileage )
        super().__init__(get_school_id, number_of_students)

    def bus_school_color(self):
        print("Bus color")

sb = SchoolBus(10,20,30,40)

# Task 7
class Bear:
    def __init__(self):
        pass

    def eat(self):
        print('Eat')


class Wolf:
    def __init__(self):
        pass

    def eat(self):
        print('Eat')

wolf = Wolf()
bear = Bear()

animals = (wolf, bear)
for animal in animals:
    animal.eat()


# Task 8
class City:
    def __new__(cls, name, population):
        if population > 1500:
            city = super().__new__(cls)
            return city

        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

d = City("n", 2000)
print(d)

