import turtle

def draw_square(some_turtle):

    # count=0
    # while count<=3:
    #     some_turtle.forward(100)
    #     some_turtle.right(90)
    #     count = count +1

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):

    some_turtle.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # Create turtle brad - draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    brad.shapesize(2, 2, 2)
    for i in range(1,34):
        draw_square(brad)
        brad.right(10)

    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.speed(1)
    # draw_circle(angie)
    #
    # peter = turtle.Turtle()
    # peter.shape("turtle")
    # peter.color("green")
    # peter.speed(1)
    # peter.shapesize(2, 2, 2)
    # draw_traingle(peter)

def terminate():
    window = turtle.Screen()
    window.exitonclick()

draw_art()
terminate()