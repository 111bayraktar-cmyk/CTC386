# ibayraktar ExtraCredit
x=1
while (x>=0):
    x=float(input("Enter the grade percentage:"))
    if (x>=90):
        print ("You have an A")
    if (x>=80) and (x<90):
        print ("You have a B")
    if (x>=70) and (x<80):
        print ("You have a C")
    if (x>=60) and (x<70):
        print ("You have a D")
    if (x<60) and (x>=0):
        print ("You have an F")

print ("You chose to exit the program.")
