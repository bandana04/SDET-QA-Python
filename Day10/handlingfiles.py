# #Example1: writing data into text file
# file = open("/home/bandana/Desktop/Automation/SDET QA/Day10/demofiles/myfile.txt",'w')
# file.write("This is my first statement...\n")
# file.write("This is my second statement...\n")
# file.write("This is my third statement...\n")
# file.write("This is my fourth statement...\n")
# file.close()
# print("program completed...")

# #EXample2: Reading data from the text file
# file = open("/home/bandana/Desktop/Automation/SDET QA/Day10/demofiles/myfile.txt",'r')
# print(file.read())
# file.close()

#EXample3 : Appending data into text file
file = open("/home/bandana/Desktop/Automation/SDET QA/Day10/demofiles/myfile.txt",'a')
file.write("This is the fifth appended statement...\n")
file.write("This is the sixth appended statement...\n")
file.close()

