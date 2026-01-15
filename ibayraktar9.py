
#ibayraktar7
#github first file!

#Option 4 is a guessing game where the user will try and guess a number until they get it correct.

#Ask a user to guess a number until they get it correct.
#Come up with a number for a user to guess and tell them to guess a number in the range of 0 to 100 inclusive.
#If the user inputs a number outside of the range, tell them to enter a number within the range.
#If they guess incorrectly, tell them if the guess was too high or too low and ask them to guess again.
#After they guess the correct number tell them they won and display a positive message.


name = input ("What is your name: ")
print  ("Menu")
print ("------***---------")
print ("Option 1")
print ("Option 2")
print ("Option 3")
print ("Option 4")
print ("-------***--------")
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
elif (option==4):
    y=54
    num=1 
    while (y!=num):
        num= int(input("Guess my number between 0-100..."))
        if (num>100) or (num<0):
            print ("Your number must be between 0-100!")
        elif (num>54) or (num==100):
            print("Pick a smaller number!")
        elif (num<54) or (num==0):
            print ("Pick a bigger number!")
        elif (num==54):
            print ("Congrats, you guess the right number!")        

else:
    print ("Choose an option between 1-4")
          



