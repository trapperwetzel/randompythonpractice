


def square_area(sidelength):
    return sidelength ** 2 
def rectangle_area(length,width):
    return length * width
def triangle_area(height,base):
    return (height * base) / 2 
def circle_area(radius):
    return 3.14 * (radius ** 2) 


usershapechoice = input("Choose a shape: Square, Rectangle, Trianagle, Circle\n")


if usershapechoice == "Square".lower():
    usersidelength = int(input("Enter the side length of your square: \n"))
    print(square_area(usersidelength))

if usershapechoice == "Rectangle".lower():
    userlength= int(input("Enter length: \n"))
    userwidth = int(input("Enter width: \n"))
    print(rectangle_area(userlength,userwidth))
    
      
if usershapechoice == "Triangle".lower():
    userheight = int(input("Enter height of triangle: \n"))
    userbase = int(input("Enter base of triangle: \n"))
    print(triangle_area(userheight,userbase))

if usershapechoice == "Circle".lower():
    userradius = int(input("Enter radius: \n"))
    print(circle_area(userradius))
