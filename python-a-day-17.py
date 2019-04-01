#!/bin/python3

# Try/except practice

def myFunc(a):
    print(1 / 0)

try:
    myFunc()
except (NameError, KeyError, IndexError):
    print("A known error occurred.")
except:
    print("An unknown error occurred.")

try:
    myFunc()
except:
    print("An error occurred.")
else:
    print("No errors occurred!")
finally:
    print("Execution has ended.")
