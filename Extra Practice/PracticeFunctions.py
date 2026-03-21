#1. Greeting Function
#Write a function that takes a name as input and prints:

def greeting(name):
    print("Hello " + name)
name = input("Enter your name: ")
greeting(name)

#2. Even or Odd
#Write a function that takes a number and returns whether it is even or odd.
def check_num(num):
    if num % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
num = int(input("Enter a number: "))
print(check_num(num))

#3. Find Maximum
#Write a function that takes a list of numbers and returns the largest number.
def largest_number(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return f"The {num1} is the largest number"
    elif num2 > num3 and num2 > num1:
        return f"The {num2} is the largest number"
    else:
        return f"The {num3} is the largest number"
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
print(largest_number(num1,num2,num3))

#4. Sum of Two Numbers
#Write a function that takes two numbers as arguments and returns their sum.
def sum_numbers(num1,num2):
    sum = num1 + num2
    return sum
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(sum_numbers(num1,num2))

#5. Count Vowels
#Write a function that takes a string and returns the number of vowels in it.
def count_vowels(text):
    vowels = "AEIOUaeiou"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count
text = input("Enter a string: ")
print(count_vowels(text))