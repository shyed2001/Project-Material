#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Shyed Shahriar Housaini
#
# Created:     07/12/2019
# Copyright:   (c) Shyed Shahriar Housaini 2019
# Licence:     <your licence, "Shyed Shahriar Housaini Terms and Conditions">
#-------------------------------------------------------------------------------
import turtle, time



turtle.color('deep pink')
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(1)
myPen.pensize(7)
window = turtle.Screen()
style = ('Courier', 300, 'italic')
message = input(''' Please enter your LETTER:


           ''')
turtle.write(message, font=style, align='center')
turtle.hideturtle()

time.sleep(1)
window.clear()
time.sleep(1)
##window.mainloop()
window.exitonclick()
