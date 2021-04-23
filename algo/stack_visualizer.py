import turtle


def draw_spiral(my_turtle, length):
    if length > 0:
        my_turtle.forward(length)
        my_turtle.right(90)
        draw_spiral(my_turtle, length - 5)


my_turtle = turtle.Turtle()
window = turtle.Screen()
draw_spiral(my_turtle, 200)
window.exitonclick()