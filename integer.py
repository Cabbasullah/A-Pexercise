#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
n=eval(input("Enter an integer: "))
val=(n+n)*(n+n)*(n*n*n)
print(val)