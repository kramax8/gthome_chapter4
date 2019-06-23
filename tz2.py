class Airplane():
    def __init__(self, make, model, year, max_speed, odometr, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = odometr
        self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True
        print('Летит... --> ')
        return self.take_off

    def land(self):
        self.is_flying = False
        print('Приземляется... <-- ')
        return self.is_flying

    def fly(self, distance):
        self.distance = distance
        if self.distance != None:
            self.odometr += self.distance

    def return_all(self):
        result = 'Марка--> ' + self.make + '| Модель--> ' + self.model
        result += '| Год--> ' + self.year + '| Max-скорость--> ' + self.max_speed
        result += '| Одометр--> ' + str(self.odometr) + ' |Состояние--> ' + str(self.is_flying)
        return result

new_plane = Airplane('Истребитель', 'Миг-3', '1980', '950 km/h', 0)

print('\t\t|Обратите внимание как меняются одометр и состояние самалета (ДО и ПОСЛЕ)| \n')

print('>ДО< ' + new_plane.return_all() + '\n')
    
new_plane.take_off()
new_plane.land()
new_plane.fly(8000)
new_plane.fly(80)

t1 = new_plane.return_all()
print('\n >ПОСЛЕ< ' + t1)
