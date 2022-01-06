import math

def sphere(radius):
    return (4/3) * math.pi * radius ** 3

radius = int(input("Enter radius (in inches): "))
print(f"Volume is {round(sphere(radius), 2)} cubic inches")
print(f"Volume is {round(sphere(radius/12), 2)} cubic feet")