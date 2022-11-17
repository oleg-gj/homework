# Task_1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print('Vehicle speed increased')

    def mileage_info(self):
        print(f'Mileage: {self.mileage}')


# Task_2
class Bus(Vehicle):
    def __int__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
