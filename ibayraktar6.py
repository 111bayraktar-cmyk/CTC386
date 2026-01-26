#ibrahim bayraktar_Lab 6

#Create a python program with the following requirements.

#Ask the user to enter their name.
#Create a menu to let a user choose from 3 different options.
#Option 1 will display a joke.
#Option 2 will display the user's name 15 times.
#Option 3 will ask the user to enter a number then display a famous quote as many times as the number they entered.

name = input ("What is your name: ")
print  ("Menu")
print ("---------------")
print ("Option 1")
print ("Option 2")
print ("Option 3")
print ("---------------")
print ("Hello", name)
option = int(input("enter a number to choose an option:"))
if (option==1):
    print ("What did 0 told to 8? Nice belt!")
elif (option==2):
    for i in range(15):
        print (name)
elif (option==3):
    x= int(input("Enter another number:"))
    for i in range(x):
        print ("Don't worry, be happy!")
else:
    print ("Choose an option between 1-3")
          



