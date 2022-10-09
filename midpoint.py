#Write a Python program to calculate midpoints of a line
x1=eval(input("Enter value of x1: "))
x2=eval(input("Enter value of x2: "))
y1=eval(input("Enter value of y1: "))
y2=eval(input("Enter value of y2: "))
mid_point=(x1+x2)/2 +(y1+y2)/2
print("Midpoint is {:,.2F}".format(mid_point))