#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
given_number1=10
given_number2=10
given_number3=10
val=given_number1+given_number2+given_number3
while given_number1 == given_number2 == given_number3:
    print(3*val)
    break
else:
    print(val)