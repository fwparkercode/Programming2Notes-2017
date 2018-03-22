import turtle

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

        spiral_fractal(size * 0.98, depth - 1)


spiral_fractal(size, 5)

my_screen.clear()

def tree_fractal(x, y, length, direction, depth):
    if depth > 0:
        my_turtle.width(depth)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.setheading(direction)
        my_turtle.down()
        my_turtle.forward(length)
        new_pos = my_turtle.pos()
        for i in range(-60, 61, 15):
            tree_fractal(new_pos[0], new_pos[1], length * 0.7, direction + i, depth - 1)



tree_fractal(0, -300, 200, 90, 4)

my_screen.exitonclick()
