# desining heart and write text.
import turtle
from turtle import*
pen = turtle.Turtle()
bgcolor("skyblue")

def curve():
	for i in range(200):
		pencolor("red")
		pen.right(1)
		pen.forward(1)
def heart():
	pen.fillcolor('red')
	pencolor("red")
	pen.begin_fill()
	pen.left(140)
	pen.forward(113)
	curve()
	pen.left(120)
	curve()
	pen.forward(112)
	pen.end_fill()
def txt():
	pen.up()
	pen.setpos(-68, 95)
	pen.down()
	pen.color('blue')
	pen.write("I love Aditya", font=("Verdana", 12, "bold"))
heart()
txt()
turtle.done()
