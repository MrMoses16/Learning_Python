# creating a class
class ClassName:
    pass

# class
class Person:
    # constructor can have default values that can be overwritten using a method
    def __init__(self, firstname = 'Kris', lastname = 'Tellez', age = '20'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.skills = []

    # Objects have methods (functions which belong to the object)
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'
    
    # Method to modify class default values
    def add_skills(self, skill):
        self.skills.append(skill)

p1 = Person()
p2 = Person('Joe', 'Mama', '69')

print(p1.name)
print(p2.person_info())
p1.add_skills('Java')
p1.add_skills('C')
p1.add_skills('Python')
print(p1.skills)

# Inheritance: can define a class the inherits all the methods and properties from parent class
# The child class inherits methods from the parent's class (can use them)
# However, the parent class cannot access methods in the child class

class Student(Person):
    pass

s1 = Student()
s1.add_skills('Python')
print(s1.person_info)
print(s1.skills)

# We do not have to call init() constructor in the child class
# When we add the init() function, the child classs will no longer inherit the parent's init()
# However, we can still access the parent's inti() by using super().method_name (can be used with all methods)

class Student(Person):
    def __init__(self, firstname='Kris', lastname='Tellez', age='20', gender = 'male'):
        self.gender = gender
        super().__init__(firstname, lastname, age)