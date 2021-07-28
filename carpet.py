import turtle 
import numpy as np
import sys

#a new data type to store a 2D coordinate (x,y)
class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y 

#calculates the midpoint of two coordinates by averaging their x and y coordinates
def midpoint(point1,point2):
  new_point_x = (point1.x + point2.x)/2
  new_point_y = (point1.y + point2.y)/2
  return Point(new_point_x,new_point_y)

#helper functions to convert radians <-> degrees
def radians_to_degrees(radian):
  return(radian * 180/np.pi)

def degrees_to_radians(degrees):
  return(degrees * np.pi/180.0)

#draws a line segment between two points in 2D
def drawLine(point1,point2):
  bob = turtle.Turtle()
  bob.penup()
  bob.hideturtle()
  bob.goto(point1.x,point1.y)
  bob.pendown()
  bob.goto(point2.x,point2.y)
  bob.penup()
  bob.goto(point1.x,point1.y)

#exploits trigonometry to draw a line starting from a point with a specified angle,
#and moves length steps in that direction. Returns the endPoint after drawing. 
def drawLineAtAngle(startPoint,angle,length):
  endPoint_x = startPoint.x + length * np.cos(degrees_to_radians(angle))
  endPoint_y = startPoint.y + length * np.sin(degrees_to_radians(angle))
  endPoint = Point(endPoint_x,endPoint_y)

  drawLine(startPoint,endPoint)
  return endPoint

#draws a triangle given three Point data objects and colors it green
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

#given side length and center point of the square
def drawSquare(centerPoint,length):
  #calculates the four vertices of the square
  bob = turtle.Turtle()
  bob.speed(10)
  bob.penup()
  bob.hideturtle()

  bottom_left = # fill here
  bottom_right = # fill here
  top_right =  # fill here
  top_left = # fill here

  bob.goto(bottom_left.x,bottom_left.y)
  bob.pendown()
  bob.fillcolor("light green")
  bob.begin_fill()
  bob.goto(bottom_right.x,bottom_right.y)
  bob.goto(top_right.x,top_right.y)
  bob.goto(top_left.x,top_left.y)
  bob.goto(bottom_left.x,bottom_left.y)

  bob.end_fill()

def sierpinski_carpet(centerPoint,length,order):
  if (order == 0):
    drawSquare(centerPoint,length)
  else:
    x = centerPoint.x
    y = centerPoint.y
    sierpinski_carpet(Point(x - 1/3*length,y - 1/3*length),length/3,order-1)
    sierpinski_carpet(Point(x,y - 1/3*length),length/3,order-1)
    sierpinski_carpet(Point(x + 1/3*length,y - 1/3*length),length/3,order-1)

    sierpinski_carpet(Point(x - 1/3*length,y),length/3,order-1)
    sierpinski_carpet(Point(x + 1/3*length,y),length/3,order-1)

    sierpinski_carpet(Point(x - 1/3*length,y+1/3*length),length/3,order-1)
    sierpinski_carpet(Point(x,y+1/3*length),length/3,order-1)
    sierpinski_carpet(Point(x + 1/3*length,y+1/3*length),length/3,order-1)

def main():
  center = Point(0,0)
  sierpinski_carpet(center,300,int(sys.argv[1]))
  turtle.done()

main()