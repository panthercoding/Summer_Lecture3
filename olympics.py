import turtle 
import numpy as np
import sys

class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y 
  

def drawCircle(centerPoint,radius,color,width):
  bob = turtle.Turtle()
  bob.penup()
  bob.pencolor(color)
  bob.width(width)
  bob.hideturtle()
  #move to a point on the radius
  bob.goto(centerPoint.x,centerPoint.y-radius)
  bob.pendown()
  #bob.fillcolor("blue")
  #bob.begin_fill()

  #start drawing 
  bob.circle(radius)
 # bob.end_fill()

def drawOlympicsLogo():
  drawCircle(Point(0,0),100,color="blue",width=10)

def main():
  drawOlympicsLogo()
  turtle.done()

main()