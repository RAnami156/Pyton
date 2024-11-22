import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(3)
t.color("red")


t.begin_fill()
t.left(50)
t.forward(100)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(100)
t.end_fill()

turtle.bye()
