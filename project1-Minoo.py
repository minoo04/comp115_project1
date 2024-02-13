#minoo esmaeili project-1
#drawing of a houce at a night

from turtle import *
import turtle
import random



speed (0)
bgcolor("forestgreen") #ground

penup()       #night sky
goto(-400, -100)
pendown()
color("navy")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

def draw_star(x, y, size):   #drawing random stars
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_random_stars(num_stars):
    for _ in range(num_stars):
        x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
        y = random.randint(0, turtle.window_height() // 2) 
        size = random.randint(10, 50)
        color = random.choice(['yellow', 'white'])
        turtle.color(color)
        draw_star(x, y, size)

draw_random_stars(25)

penup()      #moon
goto(-300, 300)
pendown()
color("lightyellow")
begin_fill()
circle(40)
end_fill()


penup() #making cloud from connected circles
goto(190, 210)
pendown()
color("lightgrey","white")
begin_fill()
circle(30) 
end_fill()

penup() 
goto(220, 250)
pendown()
color("lightgrey","white")
begin_fill()
circle(35) 
end_fill()

penup() 
goto(230, 220)
pendown()
color("lightgrey","white")
begin_fill()
circle(35) 
end_fill()

penup() 
goto(185, 215)
pendown()
color("lightgrey","white")
begin_fill()
circle(35) 
end_fill()
penup() 

penup() 
goto(170, 240)
pendown()
color("lightgrey","white")
begin_fill()
circle(40) 
end_fill()

 
penup()   #house_body
goto(-150, -150 )
pendown()
pensize(4)
color("black","brown")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

penup() #chimney
goto(0, 50)
pendown()
color("black","brown")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

penup()     #roof
goto(-150, 50)
pendown()
begin_fill()
for i in range(3):
    forward(210)
    left(120)
end_fill()

penup()   #window
goto(0,0)
pendown()
color("black","light yellow")
begin_fill()
for i in range(4):
    forward(45)
    left(90)
end_fill()

penup()
goto(0,30)
pendown()
color("black")
forward(45)
penup()
goto(25,0)
pendown()
color("black")
left(90)
forward(45)

#door

color("black","orange")
begin_fill()
penup()
goto(-30, -150)
pendown()
goto(-30, -30)
goto(30, -30)
goto(30, -150)
goto(-30, -150)
end_fill()

color("black")  #door handle
penup()
goto(15, -90)
pendown()
dot(10)

def valentines_message():
    penup()
    goto(-100, -50)
    pendown()
    color("red")
    style = ("Courier", 30, "bold")
    write("Happy Valentine's Day!", font=style, align="center")
    penup()
    goto(-102, -50)  
    pendown()
    color("pink")
    write("Happy Valentine's Day!", font=style, align="center")

valentines_message()

hideturtle()
done()                          