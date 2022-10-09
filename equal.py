#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
import math as sum

val=eval(input("Enter an integer: "))
valb=eval(input("Enter an integer: "))
valc=eval(input("Enter an integer: "))
sum=val+valb+valc
while val==valb or valb==valc or valc==val:
    print(0)
    break
else:
    print(sum)

