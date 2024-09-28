from turtle import *

#we want to paint a house

#step 1: draw a square
speed(6)
width(7)
color("green")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawin the door
forward(70)

color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

color("brown")
penup()
right(90)
pendown()
forward(60)
right(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)



color("brown")
shape("circle")
penup()
goto(79, 60)

pendown()
forward(10)

shape("arrow")


#making the roof
penup()
goto(200, 200)
pendown()

color("red")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#making the left window

penup()
goto(55, 125)
pendown()

color("blue")
width(3)
right(60)
forward(35)
right(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)

right(90)
forward(17.5)
right(90)
forward(50)

right(90)
forward(17.5)
right(90)
forward(25)
right(90)
forward(35)

#the right window

penup()
goto(180, 125)
pendown()


#copy the code from whe we were making the left window
forward(35)
right(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)

right(90)
forward(17.5)
right(90)
forward(50)

right(90)
forward(17.5)
right(90)
forward(25)
right(90)
forward(35)


#contour
color("black")

penup()
goto(0, -5)
pendown()
right(180)
forward(202)
left(90)
forward(208)
left(30)
forward(202)
left(120)
forward(205)
left(30)
forward(202)

penup()
goto(0, 200)
pendown()
left(90)
forward(200)




exitonclick()