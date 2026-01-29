print  ("Welcome!, Please choose one of the three options!")
print ("------***---------")
print ("Option 1")
print ("Option 2")
print ("Option 3")
print ("-------***--------")
option = int(input("Enter a number to choose an option:"))
if (option==1):
    name = input ("What is your name: ")
    print (name, ", why is 6 afraid of 7? Because,7 ate(8) 9! He he he!")
elif (option==2):
    for i in range(20):
        print ("Pizza!")
elif (option==3):
    y=0
    num=1 
    while (y!=num):
        num= int(input("Guess my number between 0-100..."))
        if (num>100) or (num<0):
            print ("Your number must be between 0-100!")
        elif (num>0):
            print("Pick a smaller number!")
        elif (num<0):
            print ("Pick a bigger number!")
        elif (num==0):
            print ("Congrats, you guess the right number!")
