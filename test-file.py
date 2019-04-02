import easygui_qt as easy
import turtle

window_color = easy.get_color_rgb(title="Window?")
turtle_color = easy.get_color_rgb(title="Name?")

canvas = turtle.Screen()
canvas.bgcolor(window_color)

bob = turtle.Turtle()
bob.pensize(10)
bob.color(turtle_color)
bob.forward(100)

canvas.exitonclick()
