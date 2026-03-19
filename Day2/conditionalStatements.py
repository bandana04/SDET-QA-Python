#if     if..else    elif
from dateutil.rrule import weekday

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

#Example5 : Multiple conditions using eif
weekday = int(input("Enter a weekday: "))
if weekday == 1:
    print("It is a Sunday")
elif weekday == 2:
    print("It is a Monday")
elif weekday == 3:
    print("It is a Tuesday")
elif weekday == 4:
    print("It is a Wednesday")
elif weekday == 5:
    print("It is a Thursday")
elif weekday == 6:
    print("It is a Friday")
elif weekday == 7:
    print("It is a Saturday")



