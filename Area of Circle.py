import math

def calculate_area(radius):
    if radius < 0 :
        return "Radius cannot be negative"
    return math.pi*radius*radius

try:
    radius=float(input("Enter the radius value:"))
    area=calculate_area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
except ValueError:
    print("Please enter a valid number for the radius")