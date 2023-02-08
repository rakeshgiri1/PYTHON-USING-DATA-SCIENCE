#wap for background and design.
import turtle
from turtle import*
loadWindow = turtle.Screen()
turtle.speed(0)
 
for i in range(40):
    turtle.circle(5*i,)
    turtle.circle(-5*i)
    turtle.left(i)
    bgcolor("black")
    pencolor("red")
 
turtle.exitonclick()