#ibayraktar-MidTerm-1
#Area of a triangle

base=float(input("Enter the base length of the triangle "))
height=float(input("Enter the height of the triangle "))

area=base*height/2
if (area>50):
    print ("Congrats, you have a huge triangle, with an area of ", (area))
if (area<50):
    print ("Congrats, you have a tiny traingle with an area of ", (area))

