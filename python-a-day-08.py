#!/bin/python3

# Takes inputs as strings; converts to ints for math operations, then back to strings to print

Var1= input("Type your value 1: ")
Var2= input("Type your value 2: ")

if Var1.isdigit() and Var2.isdigit():
    print(Var1 + " + " + Var2 + " = " + str(int(Var1) + int(Var2)))
    print(Var1 + " - " + Var2 + " = " + str(int(Var1) - int(Var2)))
    print(Var1 + " * " + Var2 + " = " + str(int(Var1) * int(Var2)))
    print(Var1 + " / " + Var2 + " = " + str(int(Var1) / int(Var2)))
    print(Var1 + " % " + Var2 + " = " + str(int(Var1) % int(Var2)))

else:
    print("Non-numeric input.")
