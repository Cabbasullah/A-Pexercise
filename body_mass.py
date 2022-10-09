#Write a Python program to calculate body mass index
#BIM=kg/m^2
mass=eval(input("Enter your weight: "))
height=eval(input("Enter your height: "))
Bim=mass/height**2
print("Your BIM mass is {:.3f}".format(Bim))

