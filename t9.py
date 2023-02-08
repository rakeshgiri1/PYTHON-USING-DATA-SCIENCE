from turtle import *
bgcolor("black")  
pensize(2)  
speed(0) 
while(True):
        for i in range(6): 
                for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:   
                    color(colors)  
                    circle(100)  
                    left(10)   
mainloop()  