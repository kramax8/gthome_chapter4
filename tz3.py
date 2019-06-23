class Car():
    def __init__(self, make, model, year, odometr, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = odometr
        self.fuel = fuel

    def __add_distance(self):
        self.odometr += self.distance

    def __subtract_fuel(self):
        if (self.fuel * 10) >= self.distance:
            print("Let's drive!") 
        else:
            print('Need more fuel, please, fill more')       

    def drive(self, distance):
        self.distance = distance
        if (self.fuel * 10) >= self.distance:
            self.__add_distance()
        self.__subtract_fuel()
            

new_car = Car('Mers', 'Sclass', 2010, 0, 70)

new_car.drive(700)

result = 'Одометр-> ' + str(new_car.odometr) + '\t' + 'Бензин-> ' + str(new_car.fuel)
print(result)