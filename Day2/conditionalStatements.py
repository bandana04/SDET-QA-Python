#if     if..else    elif

#Example1 : Print a person is eligible for vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You can not vote")

#Example2
if True:
    print("false condition")
else:
    print("true condition")

#Example3 : Find a number is even/odd with single statements
number = int(input("Enter a number: "))
print("It is even number") if number % 2 == 0 else print("It is odd number")

#Example4 : if else - Multiple statements in Single line
number2 = int(input("Enter a number: "))
{print("hello"), print("world")} if number2>10 else {print("bye bye"), print("world")}


