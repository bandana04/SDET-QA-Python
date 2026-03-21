#Parameterized Constructor
class Student:
    def __init__(self,name,grade,section):
        self.name = name
        self.grade = grade
        self.section = section
    def info(self):
        print(f"{self.name} studies in grade {self.grade}, section {self.section}")
student1 = Student("Ram", 1, "A")
student2 = Student("Ram", 2, "B")
student3 = Student("Ram", 3, "C")
student1.info()
student2.info()
student3.info()

#Default Constructor
class DefaultConstructor:
    def __init__(self):
        print("Default constructor doesn't accept any argument from the object")
obj1 = DefaultConstructor()

