#1. Student Class
#Create a class Student with: attributes: name, age      method: display() → prints student details
class Students:
    name = "Bandana"
    age = 25
    def display(self):
        print(f"{self.name} is {self.age} years old")
student = Students()
student1 = Students()
student.display()
student1.name = "Hanna"
student1.age = 25
student1.display()


#2. Rectangle Class
#Create a class Rectangle with: attributes: length, width    method: area() → returns area   method: perimeter() → returns perimeter
class Rectangle:
    length = 20
    width = 40
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)
rectangle_object = Rectangle()
print(rectangle_object.area())
print(rectangle_object.perimeter())


#3. Book Information
#Create a class Book with: attributes: title, author   method: show_book() → prints book details
class Book:
    title = "MunaMadan"
    author = "Laxmi Prasad Devkota"
    def show_book(self):
        print(f"The author of the book {self.title} is {self.author}")
book_object = Book()
book_object.show_book()
book_object1 = Book()
book_object1.author = "Bandana Limbu"
book_object1.title = "Kalpana"
book_object1.show_book()

#4. Bank Account
#Create a class BankAccount with: attribute: balance    method: deposit(amount)  method: withdraw(amount)   method: display_balance()
class BankAccount:
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.balance} deposited.")
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
            print(f"{self.balance} withdrawn.")
        else:
            print("Insufficient balance")
    def display_balance(self):
        print(f"Current balance is {self.balance}")
account_object = BankAccount()
account_object.balance = 1000
account_object.deposit(400)
account_object.withdraw(600)
account_object.display_balance()

#5. Calculator Class
# Create a class Calculator with: method: add(a, b) → returns sum  method: multiply(a, b) → returns product
class Calculator:
    def add(self,num1,num2):
        Add = num1 + num2
        return Add
    def multiply(self,num1,num2):
        Multiply = num1 * num2
        return Multiply
add_object = Calculator()
multiply_object = Calculator()
print(add_object.add(10,20))
print(multiply_object.multiply(10,20))


