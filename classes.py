import datetime
from datetime import date
# today = datetime.date.today()
# year = today.year


class Student:
    school = 'AkiraChix'

    def __init__(self, first_name, last_name, age, country):
        self.name1 = first_name
        self.name2 = last_name
        self.age = age
        self.nationality = country

    def greet_student(self):
        return f"Hello {self.name1}, welcome to {self.school}"
    
    def year_of_birth(self):
        year = datetime.date.today().year
        years = year - self.age
        return f"Hello {self.name1}, you were born in {years}"
    
    def show_full_name(self):
        return f"{self.name1} {self.name2}"

    def show_initials(self):
        return f"{self.name1[0]}.{self.name2[0]}"



student1 = Student("Esther", "Mwangi", 16, "Kenya")
# student2 = Student("MaryAnne", "Muthoni", 22,"Rwanda")
student3 = Student("Grusha", "Vashnadze", 23, "Tanzania")

print(student1.show_full_name())
print(student1.year_of_birth())
print(student1.show_initials())

print(student3.show_full_name())
print(student3.year_of_birth())
print(student3.show_initials())






  