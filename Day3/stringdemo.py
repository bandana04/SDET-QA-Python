#Ways of creating string variables
r = 'welcome'
s = "welcome"
t = str("welcome")
u = str('welcome')

#ways of creating empty string variables
name = ""
age = ''
address = str()

#mutable - can change the value of variable
#immutable - cannot change the value of variable
#strings are immutable, meaning its value cannot be changed

str1 = "hello"
print(id(str1))

str2 = str1 + "world"
print(id(str2))

#Example3 :  * with string
str3 = "welcome"
print(str3*10)

#EXample4 : slicing[]
#starting index 0
#ending index 1
str4 = "welcome"
print(str4[1:3])
print(str4[:5])
print(str4[2:])
print(str4[:])
print(str4[1:-1])
print(str4[1:-2])

#EXample5 : ASCII Num --> ord(), ASCII character --> chr()
print(ord('A'))
print(chr(65))

#Example6 : max() min() len()
print(max("abc"))
print(min("abc"))
print(len("abc"))

#Example7 : in, not in operators - returns true/false
y = "welcome"
print("come" in y)
print("lome" in y)
print("come" not in y)
print("lome" not in y)

#EXample8: String comparison
print("tim"=="tie")
print("free" != "freedom")
print("arrow">"aron")
print("right">="left")
print("teeth"<"tee")
print("yellow"<="fellow")
print("abc">"")

#Example9 : Testing Strings True/False
v = "welcome to python"
print(v.isalnum())
print(v.isalpha())
print(v.isdigit())
print(v.isidentifier())
print(v.isprintable())
print(v.isspace())
print(v.isupper())

#EXample10 : Searching for substrings
w = "welcome to python"
print(w.endswith("python"))
print(w.startswith("python"))
print(w.find("python"))
print(w.count("o"))

#Example11 : Converting string
e = "string in python"
print(e.capitalize())
print(e.title())
print(e.lower())
e1 = w.swapcase()
print(e1)
print(e.replace("python", "python2"))

#Reverse string
#Method1
f = "bandana"
rev_str = ""
for i in f:
    rev_str = i + rev_str
print("reversed string is:", rev_str)
#Method2
g = "kaairu"
rev_str = g[::-1]
print(rev_str)





