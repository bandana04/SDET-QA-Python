#Check the given number is Positive or negative
num1 = int(input("Enter a number: "))
if num1 >= 0:
    print("It is positive number")
else:
    print("It is negative number")

#Check the largest of 2 numbers
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num2 > num3:
    print("Num2 is largest number")
else:
    print("Num3 is largest number")

#CHeck the largest of 3 numbers
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
if num4 > num5 and num4 > num6:
    print("Num4 largest among 3")
elif num5 > num4 and num5 > num6:
    print("Num5 largest among 3")
else:
    print("Num6 largest among 3")

#Print week number if you provide weekname as input
weekday = input("Enter a weekday: ")
if weekday == "Sunday":
    print("The week number is 1")
elif weekday == "Monday":
    print("The week number is 2")
elif weekday == "Tuesday":
    print("The week number is 3")
elif weekday == "Wednesday":
    print("The week number is 4")
elif weekday == "Thursday":
    print("The week number is 5")
elif weekday == "Friday":
    print("The week number is 6")
elif weekday == "Saturday":
    print("The week number is 7")
