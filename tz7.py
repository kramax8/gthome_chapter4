class Student():
    def __init__(self, full_name, age, major):
        self.full_name = full_name
        self.age = age
        self.major = major

    def __str__(self):
        s_about = '<name: ' + self.full_name + ', age: ' + str(self.age) + ', major: ' + self.major.title() +' >'
        return s_about

Steve = Student('Stiven Schultz', 23, 'english')
Johnny = Student('Jonathan Rosenberg', 24, 'biology')
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')
print(Penny)