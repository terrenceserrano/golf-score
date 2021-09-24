#create a program that will print a golf score(par, stroke)

#table of conditions
# if strokes = par
# 1 = " hole in one "
# <= par -2 = "Eagle"
# par -1 = "Birdie"
# par = "par"
# par +1 = "Bogey"
# par +2 = "Double Bogey"
# >= par +3 = "Go Home"

par = int(input("Input par score here: "))
stroke = int(input("Input stroke score here: "))
golf_score = par, stroke

if stroke == 1:
    print("Hole in one")
elif stroke <= par - 2:
    print("Eagle")
elif stroke == par - 1:
    print("Birdie")
elif stroke == par:
    print("par")
elif stroke == par + 1:
    print("Bogey")
elif stroke == par + 2:
    print("Double Bogey")
elif stroke >= par + 3:
    print("Go home")
else:
    print("Change player")


