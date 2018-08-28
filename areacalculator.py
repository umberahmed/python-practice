"""Area Calculator is useful for doing math and can be used to automate many calculations"""

print "Let's use this area calculator"

name = raw_input("What's your name? ")

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
    radius = float(raw_input("What is the radius of the circle you'd like to calculate: "))
    area = 3.14159 ** radius
    print name.title() + ", the area of your circle is " + str(area)
elif option == "T":
    base = float(raw_input("What is the base of the triangle you'd like to calculate? "))
    height = float(raw_input("What is the height of the triable you'd like to calculate? "))
    area = 0.5 * base * height
    print name.title() + ", the area of your triangle is " + str(area) + "."
else:
    print "That's an incorrect shape."
