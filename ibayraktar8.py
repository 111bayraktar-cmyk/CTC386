
#ibayraktar8.py
#Option 5 will call a function you defined at the beginning of your program. The function will have the following requirements.

#Ask the user to enter the current temperature in Fahrenheit.
#Calculate what the value is in Celsius.
#Display the result.
#Formula for the conversion is °C = [°F - 32] × (5/9)

name = input ("What is your name: ")
print  ("Menu")
print ("------***---------")
print ("Option 1")
print ("Option 2")
print ("Option 3")
print ("Option 4")
print ("Option 5")
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
          
elif (option==5):
    def temp1(x):
        temp2=((x-32)*5/9)
        return temp2
    y=float(input("Enter the current temperature in Fahreneit:"))
    output = temp1(y)
    print ("The temperature in Celcius is ", output)

else:
    print ("Choose an option between 1-5")
