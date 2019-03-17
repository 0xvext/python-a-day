#!/bin/python3

# Differentiates between strings and ints, but not floats

Var1= input("Type your value 1: ")
Var2= input("Type your value 2: ")

if Var1.isdigit():
    print("Var1: Numeric.")
else:
    print("Var1: Non-numeric.")

if Var2.isdigit():
    print("Var2: Numeric.")
else:
    print("Var2: Non-Numeric.")
