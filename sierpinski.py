import turtle 
import numpy as np
import sys

class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y 

def midpoint(point1,point2):
  new_point_x = (point1.x + point2.x)/2
  new_point_y = (point1.y + point2.y)/2
  return Point(new_point_x,new_point_y)

def drawTrianglePoints(point1,point2,point3):
  bob = turtle.Turtle()
  bob.penup()
  bob.hideturtle()
  bob.goto(point1.x,point1.y)
  bob.pendown()
  bob.fillcolor("light green")
  bob.begin_fill()

  bob.goto(point2.x,point2.y)
  bob.goto(point3.x,point3.y)
  bob.goto(point1.x,point1.y)
  bob.end_fill()

#  turtle.done()

"""
point1 = Point(100,0)
point2 = Point(0,100)
point3 = Point(0,0)
drawTrianglePoints(point1,point2,point3)
"""

def drawSierpinski(point1,point2,point3,order):
  if (order == 0):
    drawTrianglePoints(point1,point2,point3)

  else: #draw three inner Sierpinski triangles of order-1
    drawSierpinski(point1,midpoint(point1,point2),midpoint(point1,point3),order-1)
    drawSierpinski(point2,midpoint(point2,point3),midpoint(point2,point1),order-1)
    drawSierpinski(point3,midpoint(point3,point1),midpoint(point3,point2),order-1)

p1 = Point(-150,-130)
p2 = Point(150,-130)
p3 = Point(0,130)
order = int(sys.argv[1])
drawSierpinski(p1,p2,p3,order)
turtle.done()