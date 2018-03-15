import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')

# draw a shape using goto
my_turtle.fillcolor("red")
my_turtle.begin_fill() # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()  # end of shape

# pick up the turtle
my_turtle.up()
my_turtle.goto(200, 200)

my_turtle.down()
my_turtle.fillcolor("blue")
my_turtle.begin_fill()
my_turtle.goto(300, 300)
my_turtle.goto(300, 200)
my_turtle.goto(200, 200)
my_turtle.end_fill()

# draw using headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(4)  # width in pixels

my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.end_fill()

my_turtle.fillcolor("green")
my_turtle.begin_fill()
for i in range(6):
    my_turtle.right(60)
    my_turtle.forward(100)
my_turtle.end_fill()


# Rectangle recursive pattern
my_screen.clear()


my_turtle.home()


def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)
        my_turtle.down()
        my_turtle.goto(width / 2, -height / 2)
        my_turtle.goto(-width / 2, -height / 2)
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.goto(width / 2, height / 2)
        recursive_rect(width / 2, height / 2, depth - 1)

my_turtle.width(2)
recursive_rect(1000, 600, 10)

my_screen.clear()


# Recursive Fractal (ncaa)
import random
def recursive_ncaa(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size / 2)
        my_turtle.goto(x + size, y - size / 2)
        size = random.random() * size
        recursive_ncaa(x + size, y + size, size, depth - 1)
        recursive_ncaa(x + size, y - size, size, depth - 1)


recursive_ncaa(-300, 0, 250, 7)


my_screen.exitonclick()





















'''# other turtle functions/methods that might help you
my_turtle.hideturtle()
my_turtle.backward()  # if you are using heading control
print(my_turtle.xcor(), my_turtle.ycor())
print(my_turtle.position())
my_screen.clear()
my_turtle.clone()



# squares recursion
my_screen.clear()
my_turtle.width(2)

def square(depth, size):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(size, size)
        my_turtle.down()
        my_turtle.goto(-size, size)
        my_turtle.goto(-size, -size)
        my_turtle.goto(size, -size)
        my_turtle.goto(size, size)
        square(depth - 1, size * 1.5)

square(20, 4)

def ncaa_fractal(x, y, size, depth):
    my_turtle.up()
    if depth > 0:
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y - size / 2)
        my_turtle.goto(x + size, y + size / 2)

        ncaa_fractal(x + size, y - size / 2, size / 2, depth - 1)
        ncaa_fractal(x + size, y + size / 2, size / 2, depth - 1)

my_screen.clear()
ncaa_fractal(-350, 0, 300, 8)

my_screen.exitonclick()  # end of program

'''








