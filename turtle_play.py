import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_screen = turtle.Screen()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

x = 0
y = 0
size = 500


def spiral_fractal(size, depth):
    if depth >= 0:
        my_turtle.up()
        my_turtle.width(1)
        my_turtle.color(color_list[depth % len(color_list)])
        my_turtle.begin_fill()
        my_turtle.goto(0, 0)
        my_turtle.down()
        my_turtle.forward(size)
        my_turtle.right(90)
        my_turtle.forward(size)
        my_turtle.right(90)
        my_turtle.forward(size)
        my_turtle.right(90)
        my_turtle.end_fill()
        my_turtle.forward(size)
        my_turtle.right(97)

        spiral_fractal(size * 0.90, depth - 1)


#spiral_fractal(size, 50)



def tree_fractal(x, y, length, direction, thick, color, depth):
    if depth > 0:

        sag = 90 - my_turtle.heading()

        my_turtle.width(thick)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.setheading(direction)
        my_turtle.down()
        bends = random.randrange(1,10)
        for i in range(bends):
            my_turtle.left(random.randrange(-6,7))
            my_turtle.forward(length/bends)
        new_pos = my_turtle.pos()
        new_branches = random.randrange(3, 6)
        for i in range(new_branches):
            tree_fractal(new_pos[0], new_pos[1], length * max(random.random(), 0.6), direction + random.randrange((i + 1) * 15) * random.choice([-1, 1]), thick/1.7, color, depth - 1)
    else:
        if random.randrange(15) == 0:
            my_turtle.width(1)
            my_turtle.fillcolor(color)
            for i in range(4):
                my_turtle.begin_fill()
                my_turtle.circle(4, 360, 8)
                my_turtle.end_fill()
                my_turtle.right(90)


my_screen.clear()
my_turtles = [turtle.Turtle() for x in range(3)]
for my_turtle in my_turtles:
    my_turtle.speed(0)
    my_turtle.goto(0, -325)

    my_turtle.down()
    my_turtle.pencolor("black")
    my_screen.clear()

    my_turtle.setheading(90)

    for i in range(1, 8):
        my_turtle.forward(150)
        my_turtle.right(random.randrange(-5, 6))
        my_turtle.backward(150)
        my_turtle.width(i * 4 + 5)

    my_turtle.forward(150)
    color = random.choice(["red", "pink", "lightblue", "orange", 'white', "blue"])
    tree_fractal(my_turtle.xcor(), my_turtle.ycor(), 150, 90, 20, color, 6)



my_screen.exitonclick()
