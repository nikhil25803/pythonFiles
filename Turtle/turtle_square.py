from turtle import*
import turtle


t=turtle.Turtle()
n=50
for i in range(0,50,10):
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n-i)





turtle.done()