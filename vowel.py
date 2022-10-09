#Write a Python program to test whether a letter is a vowel or not
list=("A", "a","E","e","i","I","o","0","u", "U")
letter=input("Enter any character: ")
if letter in list:
    print("It is vowel")
else:
    print("It is not a vowel")