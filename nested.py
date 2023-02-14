from turtle import *
speed(0)
pencolor('green')
fillcolor('red')
pensize(5)
side=6
for i in range (side):
    fd(75)
    begin_fill()
    for i in range (side):
       fd(75) 
       for i in range (side):
          fd(75/2)
          lt(360/side)
          dot(15)
       rt(360/side)  
    end_fill() 
ht()
mainloop()
    