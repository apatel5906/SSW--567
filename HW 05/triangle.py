#Arpit Patel
# Classifying Triangle
def classify_triangle(a, b, c):

# Invalid Inputs
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "Invalid Input"
    x = int(a)
    y = int(b)
    z = int(c)
# Checking if the values are 0
    if x<=0 or y<=0 or z<=0:
        return "Invalid Input"
# Checking the Condition to be a Triangle
    if x + y <= z or y + x <= z or x + z <= y:
        return "Not a Triangle"
# Equilateral Triangle
    if x == y == z:
        return "Equilateral"
# Isosceles Triangle
    elif x == y or y == z or z == x:
        return "Isosceles"
# Right Angle Triangle
    elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        return "Right"
# Scalene Triangle
    elif x != y and y != z and x != y:
        return "Scalene"


