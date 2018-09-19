import os

#We use the input function to take an input
#We have to have an assignment statement to store an input

#input is a function. It runs a small program that causes
#the computer to stop and wait for input
fName = input ("what is your name: ")
lName = input ("What is your last name: ")

print("Hi, "+fName+" "+lName)

initialName = fName[0] + "." + lName  #adding strings is concatination
print("Hello my good sir, "+initialName)

os.system("say "+fName+" "+lName)
