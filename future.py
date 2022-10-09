#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
#fv=pr(1+r)^n FV=pr(1+(R×T))
present_value=eval(input("Enter amount: "))
interest_rate=eval(input("Enter rate of interest (%): "))
n=eval(input("Enter number of years: "))
future_value=present_value*(1+(interest_rate)*0.01)**n

print("Future value is {:.4f}".format(future_value))