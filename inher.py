
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} years old"
class employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} and  My employee ID is {self.employee_id}."
class coruse:
    def __init__(self, course_name):
        self.course_name = course_name
        

    def course_info(self):
        return f"Course Name: {self.course_name}"
class inernship_employee(employee, coruse):
    def __init__(self, name, age, employee_id, course_name, internship_duration):
        employee.__init__(self, name, age, employee_id)
        coruse.__init__(self, course_name)
        self.internship_duration = internship_duration

    def introduce(self):
        base_introduction = super().introduce()
        course_information = self.course_info()
        return f"{base_introduction}\n{course_information}\nInternship Duration: {self.internship_duration} months"

name =  input("Enter your name: ")
age = int(input("Enter your age: "))
employee_id = input("Enter your employee ID: ")
course_name = input("Enter your course name: ")
internship_duration = int(input("Enter your internship duration in months: "))
Ebin = inernship_employee(name, age, employee_id, course_name, internship_duration)
print(Ebin.introduce())