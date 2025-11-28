
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

name =  input("Enter your name: ")
age = int(input("Enter your age: "))
employee_id = input("Enter your employee ID: ")
Ebin = employee(name, age, employee_id)
print(Ebin.introduce())