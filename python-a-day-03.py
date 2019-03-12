#!/bin/python3

# This version takes only strings
# TODO: Dynamically detect input type

Var1 = input("Type your first value: ")
Var2 = input("Type your second value: ")

print("Type(Var1): " + str(type(Var1)))
print("Type(Var2): " + str(type(Var2)))

print(Var1 + Var2)
