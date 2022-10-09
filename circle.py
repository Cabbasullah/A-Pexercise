#Write a Python program which accepts the radius of a circle from the user and compute the area
import math

radius=eval(input("Enter redius: "))
Area=float (math.pi*(radius**2))
print("Area of the circle is {: .4f}".format(Area))