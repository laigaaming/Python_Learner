import turtle

def draw_traingle(some_turtle):

    count = 0
    while count <= 2:
        some_turtle.forward(100)
        some_turtle.right(120)
        count = count + 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # Create turtle brad - draw a square
    # brad = turtle.Turtle()
    # brad.shape("turtle")
    # brad.color("yellow")
    # brad.speed(10)
    # brad.shapesize(2, 2, 2)
    # for i in range(1,34):
    #     draw_square(brad)
    #     brad.right(10)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.speed(1)
    # draw_circle(angie)
    #
    # Create turtle peter - draw a traingle
    peter = turtle.Turtle()
    peter.shape("turtle")
    peter.color("green")
    peter.speed(10)
    peter.shapesize(2, 2, 2)
    for i in range(1,34):
        draw_traingle(peter)
        peter.right(10)

def terminate():
    window = turtle.Screen()
    window.exitonclick()

draw_art()
terminate()