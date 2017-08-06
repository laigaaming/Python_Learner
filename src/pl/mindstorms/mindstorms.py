import turtle

def draw_square(some_turtle):

    count=0
    while count<=3:
        some_turtle.forward(100)
        some_turtle.right(90)
        count = count +1

def draw_circle(some_turtle):

    some_turtle.circle(100)

def draw_traingle(some_turtle):

    count = 0
    while count <= 2:
        some_turtle.forward(100)
        some_turtle.right(120)
        count = count + 1


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)
    brad.shapesize(2, 2, 2)
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(1)
    draw_circle(angie)

    peter = turtle.Turtle()
    peter.shape("turtle")
    peter.color("green")
    peter.speed(1)
    peter.shapesize(2, 2, 2)
    draw_traingle(peter)

def terminate():
    window = turtle.Screen()
    window.exitonclick()

# draw_square()
# draw_circle()
# draw_traingle()
draw_art()
terminate()
