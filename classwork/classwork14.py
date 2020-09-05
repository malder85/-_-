from person import Person

person_john = Person("John", "01/03/1984", "male")

print(person_john.name)

class Student(Person):
    def chage_name(self):
        if "student" not in self.name:
            self.name = "student" + self.name

class Employer(Person):
    def chage_name(self):
        if "Employer" not in self.name:
            self.name = "Employer" + self.name

student_john = Student("John", "01/03/1984", "male")
employer_jane = Employer("Jane", "21/10/2001", "female")
print(student_john.name, student_john.get_age())
student_john.chage_name()
print(student_john.name)
employer_jane.chage_name()
print(employer_jane.name)