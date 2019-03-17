#!/bin/python3

# Do something with loops and ifs 

Var1= input("Type your value 1: ")

for i in range(1, 21):
    if Var1.isdigit():
        print(Var1 + " + " + str(i) + " = " + str(int(Var1) + i))
        print(Var1 + " - " + str(i) + " = " + str(int(Var1) - i))
        print(Var1 + " * " + str(i) + " = " + str(int(Var1) * i))
        print(Var1 + " / " + str(i) + " = " + str(int(Var1) / i))
        print(Var1 + " % " + str(i) + " = " + str(int(Var1) % i))
    else:
        print("Non-numeric input.")
