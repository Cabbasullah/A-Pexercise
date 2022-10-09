#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
#formula:  d=√((x2 – x1)² + (y2 – y1)²).  (7, 8) and (-8, 0)
import math
x1=eval(input("Enter value of x1: "))
x2= eval(input("Enter value of x2: "))
y1=eval(input("Enter value of y1: "))
y2=eval(input("Enter value of y2: "))

distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("The distance between the points is,{:.3f}".format(distance))