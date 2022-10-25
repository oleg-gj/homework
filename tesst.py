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