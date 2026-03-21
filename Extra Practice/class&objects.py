class students:
    name = "Bandana"
    age = 26
    occupation = "QA"
    def info(self):
        print(f"{self.name} is {self.age} years old. She is {self.occupation}")
Student1 = students()
Student2 = students()
Student2.info()
Student2.name = "Kaairu"
Student2.age = 4
Student2.occupation = "Pet"
Student2.info()
