#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. 
given_number=eval(input("Enter a number: "))
difference=given_number-17


while given_number>17:
    print(2*difference)
    break
else:
    print(difference)