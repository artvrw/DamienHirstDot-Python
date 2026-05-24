import random
import colorgram
import turtle as t
colors = colorgram.extract('photo.jpg', 100)
kolory = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    kolory.append((r, g, b))
timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.goto(-400, -340)
def line():
    for _ in range(10):
        timmy.pendown()
        timmy.color(random.choice(kolory))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
for _ in range(10):
    line()
    timmy.backward(500)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
screen = t.Screen()
screen.exitonclick()
