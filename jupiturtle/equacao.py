import turtle
import numpy as np

t = turtle.Turtle()
t.speed(0)
t.color("red", "red") 

turtle.bgcolor("white")

t.penup()
for teta in np.linspace(0, 2*np.pi, 1000):
    x = 16 * (np.sin(teta)**3)
    y = 13*np.cos(teta) - 5*np.cos(2*teta) - 2*np.cos(3*teta) - np.cos(4*teta)
    t.goto(x*10, y*10)  
    t.pendown()

turtle.done()