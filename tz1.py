class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def result(self):
        result_str = self.name + ' ' + self.lastname + ' поступил в '
        result_str += self.year_of_entrance + ' г. на факультет: '
        result_str += self.department
        return result_str

new_student = Student('Вася', 'Иванов', 'Программирование', '2017')

print(new_student.result())