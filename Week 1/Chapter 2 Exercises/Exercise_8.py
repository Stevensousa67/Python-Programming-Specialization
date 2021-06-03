# Write a program that will compute the area of a circle. Prompt the user to enter the radius and save it to avariable
# called radius. Print a nice message back to the user with the answer.
import math

radius = int(input("Enter radius of circle: "))
area = math.pi * (radius**2)
area = round(area, 2)

print(area)
