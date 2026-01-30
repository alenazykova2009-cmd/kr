#class Employee:
#    def __init__(self, name, position):
#        self.name = name
#        self.position = position
#    def display_info(self):
#        print(f"Сотрудник: {self.name}, Должность: {self.position}")
#employee = Employee("Нвстя", "Менеджер")
#employee.display_info()



#class Team:
#    def __init__(self):
#        self.team_members = []
#    def add_member(self, name, position):
#        member_data = [name, position]
#        self.team_members.append(member_data)
#        print(f"Сотрудник {name} добавлен в команду")
#    def show_team(self):
#        print("Список команды: ")
#        if not self.team_members:
#            print("В команде пока никого нет.")
#        else:
#            for member in self.team_members:
#                print(f"Имя: {member[0]}, Должность: {member[1]}")
#team = Team()
#team.add_member("Маша", "Строитель")
#team.add_member("Юля", "Дизайнер")
#team.show_team()

class Book:
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year =year
    def get_name(self):
        return self.__name
    def get_author(self):
        return self.__author
    def get_year(self):
        return self.__year
    def set_name(self, name):
        self.__name = name
    def set_author(self, author):
        self.__author = author
    def set_year(self, year):
        self.__year = year
    def display_info(self):
        print(f"Название: {self.__name}, Автор: {self.__author} Год: {self.__year}")
book = Book("Детство", "Толстй", 1852)
book.display_info()

book.set_year(1234)
print(f"Год: {book.get_year()}")

