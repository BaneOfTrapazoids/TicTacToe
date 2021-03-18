#READ THIS SECTION
#This python program will select a random shape ranging from a triangle to a heptadecagon (17 sides), and then begin to draw the shape in a spiral pattern, if you want to restart then click the button in the top right corner that says "stop", then click it again. Some of the shapes after nonagon don't quite work right though
#READ THIS SECTION
import turtle
from random import randint
my_turtle = turtle.Turtle()

my_turtle.speed(0)
turtle.colormode(255)
my_turtle.pensize(10)
my_turtle.fillcolor(0,0,0)



shape_angle_dict = {
    "triangle":120,
    "square":90,
    "pentagon":72,
    "hexagon":60,
    "heptagon":51.429,
    "octagon":45,
    "nonagon":40,
    "decagon":36,
    "hendecagon":32.72727273,
    "dodecagon":30,
    "tridecagon":27.692,
    "tetradecagon":25.714285714,
    "pentadecagon":24,
    "hexadecagon":22.5,
    "heptadecagon":21.18
}

shape_random_num = randint(0,14)
shapes = ["triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon", "hendecagon", "dodecagon", "tridecagon", "tetradecagon", "pentadecagon", "hexadecagon", "heptadecagon"]
angle = shape_angle_dict[shapes[shape_random_num]]
print(angle)
print(shapes[shape_random_num])
for i in range(800):
    my_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    my_turtle.forward(i)
    my_turtle.right(angle)

turtle.done()