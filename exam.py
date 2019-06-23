class Restaurant():
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def describe_rest(self):
        rest_about = self.rest_name + ' ' + self.cuisine_type
        return rest_about

    def open_rest(self):
        return 'Ресторан открыт... '

new_rest = Restaurant('SHIFU', 'CHINA')

print(new_rest.open_rest())