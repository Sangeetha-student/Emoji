#Python program to draw smile face emoji
#using turtle

import turtle,time
#turtle object
pen=turtle.Turtle()

print("Face with Stuck-Out Tongue Emoji :)")
#function for creation of eye
def eye(col,rad):
  pen.down()
  pen.fillcolor(col)
  pen.begin_fill()
  pen.circle(rad)
  pen.end_fill
  pen.up()
  
  #draw face
  pen.fillcolor('yellow')
  pen.begin_fill
  pen.circle(100)
  pen.end_fill()
  pen.up()
  
  #draw eyes with the help of eye function
  #declared above
  pen.goto(-40,120)
  eye('white',15)
  pen.goto(-37,125)
  eye('black',5)
  pen.goto(40,120)
  eye('white',15)
  pen.goto(40,125)
  eye('black',5)
  
  #draw nose(using eye function)
  pen.goto(0,75)
  eye('black',8)
  
  #draw mouth
  pen.goto(-40,85)
  pen.down()
  pen.right(90)
  pen.circle(40,180)
  pen.up()
  
  #draw tongue
  pen.goto(-10,45)
  pen.down()
  pen.right(180)
  pen.fillcolor('red')
  pen.begin_fill()
  pen.circle(10,180)
  pen.end_fill()
  pen.hideturtle()
  
  #after creating smile emoji, output gets to stop for that, time module is used
  time.sleep(10)
