"""Calculate and print the area of the circle based on the user's input of the circle's radius"""

#user input--->taking the input only as int type
radius=float(input("Input the radius of the circle :"))

#calculating the area of the circle
area=3.14159*(radius**2)

#output
print(" The area of the circle with radius",radius,"is:",area)