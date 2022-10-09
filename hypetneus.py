#Write a Python program to calculate the hypotenuse of a right angled triangle
# formula: hypotenouse= √(a² + b²)
import math
side_a=eval(input("Enter side a: "))
side_b=eval(input("Enter side b: "))
hypotenuse=math.sqrt(side_a**2+side_b**2)
print("The hypotneus of this triangle is {:.3f}".format(hypotenuse))