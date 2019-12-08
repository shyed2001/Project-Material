#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shyed Shahriar Housaini
#
# Created:     07/12/2019
# Copyright:   (c) Shyed Shahriar Housaini 2019
# Licence:     <your licence, "Shyed Shahriar Housaini Terms and Conditions">
#-------------------------------------------------------------------------------

import turtle, time
import random
from alphabet import alphabet

message = input(''' Please enter your LETTER:


           ''')

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(3)
myPen.pensize(7)
window = turtle.Screen()
window.bgcolor("#000000")

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()

  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()

      x += fontSize

    if character == " ":
      x += fontSize
    x += characterSpacing

#Main Program Starts Here
fontSize = 250
characterSpacing = 5
fontColor = "#FF00FF"


time.sleep(1)
displayMessage(message,fontSize,fontColor,-190,0)
time.sleep(7)
window.clear()
time.sleep(1)
##window.mainloop()
window.exitonclick()