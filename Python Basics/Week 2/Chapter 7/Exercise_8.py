# Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a
# regular polygon. The program should draw the polygon and then fill it in

import turtle

number_sides = int(input("Enter amount of sides (larger than 3): "))
length_of_sides = int(input("Enter length of sides: "))
color = input("Enter color to fill in polygon: ")
rotation = 360//number_sides

wn = turtle.Screen()
breski = turtle.Turtle()
breski.pencolor(color)
breski.fillcolor(color)
breski.begin_fill()

for turn in range(number_sides):
    breski.forward(length_of_sides)
    breski.left(rotation)

breski.end_fill()
wn.exitonclick()
