#Write a Python program to check whether a specified value is contained in a group of values.
list=("6,7,8,9,0,2,6,12,98,35")
value=input("inter a value: ")
if value in list:
    print("This number is on the list.")
else:
    print("Opps!!! This is not on the list")
