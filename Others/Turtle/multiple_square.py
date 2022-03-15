from turtle import*
import turtle



def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)



def squares(beg_size,numbers):
    for i in range(0,numbers):
        size=(i+1)*beg_size
        square(size)

t=turtle.Turtle()

squares(10,10)




turtle.done()
