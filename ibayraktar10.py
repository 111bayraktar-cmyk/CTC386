
#ibayraktar10.py
#The sixth option for your menu will be a custom option of your choosing 
#with the following requirements.

#Include a loop.
#Include a conditional statement.
#Include user input.
#Include a function.
#Push your final project to your GitHub account from the class server.


name = input ("What is your name: ")
print  ("Menu")
print ("------***---------")
print ("Option 1")
print ("Option 2")
print ("Option 3")
print ("Option 4")
print ("Option 5")
print ("Option 6")
print ("-------***--------")
print ("Hello", name)
option = int(input("Enter a number to choose an option:"))
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
          
elif (option==5):
    def temp1(x):
        temp2=((x-32)*5/9)
        return temp2
    y=float(input("Enter the current temperature in Fahreneit:"))
    output = temp1(y)
    print ("The temperature in Celcius is ", output)

elif (option==6):
    print ("Now it is time to celebrate your birthday!")
    x=12
    month=9
    while (x!=month):
        month=int(input("Select your birth month's number, 1-12:"))
        x=month
        if (month>1) or (month<1):
            print ("Your birthday is not yet!")
        elif (month==1):
            print ("It is time to sing your birthday song!")
            def song():
                print ("Happy birthday to you,")
                print ("Happy birthday to you,")
                print ("Happy birthday to you dear",name)
                print ("Happy birthday to you,")
                print (" ")
            for i in range(2):
                song()
        print("Good bye") 

else:
    print ("Choose an option between 1-6")
