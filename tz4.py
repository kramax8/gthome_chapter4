
class ContactList(list):
    def __init__(self, c_list):
        self.c_list = c_list
    def search_by_name(self, name):
        self.name = name
        self.all_contacts = []
        for i in self.c_list:
            if i == self.name:
                self.all_contacts.append(self.name)
        return self.all_contacts
        self.all_contacts = ContactList()



a = ContactList(['afsadf', 'jdsaf', 'john', 'dsfa', 'john'])
print(a.search_by_name('john'))