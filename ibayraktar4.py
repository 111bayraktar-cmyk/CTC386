#Ibrahim Bayraktar
# Lab 4

#Create a python program to do the following.

#Ask a user to enter a number that represents a score on a test.
#Display the letter grade that corresponds to the score entered.
#Run your program to test all possible grade outcomes.

x =float(input("Enter your test score: "))
if (x>=90):
    print ("Your grade is an A!")
elif (x<90) and (x>=80):
    print ("Your garde is a B!")
elif (x<80) and (x>=70):
    print ("Your grade is a C!")
elif (x<70) and (x>=60):
    print ("Your grade is a D!")
else:
    print ("Your grade is an F!")

