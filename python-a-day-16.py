#!/bin/python3

# Combining pieces

import os

# Get the terminal size and store into variables
rows, columns = os.popen('stty size', 'r').read().split()

# TODO: Convert rows and columns to ints (currently strs) and if columns is even, reduce by 1

# Message to print
testString = "This is a message."

# Print a single # with no line break
def printHash():
    print("#", end="")

# Print blank space around the message
def printBuffer(a):
    for i in range((int(columns) - 2 - len(a)) // 2):
        print(" ", end="")

# Print vertical # to height of box
def printColumn(height):   
    # If height of box is an even number, add 1
    if height % 2 == 0:
        height += 1

    for i in range(height):
       printHash()
       for i in range(int(columns) - 2):
           print(" ", end="")
       printHash()
       print()

# Print a row of # to fill width
def printRow():
    for i in range(int(columns)):
        print("#", end="")
    print()

# Draw a box with the message inside
def printMessage(a, b = 0):
    printRow()
    printColumn(b // 2)
    printHash()
    printBuffer(a)
    print(a, end="")
    printBuffer(a)
    printHash()
    print()
    printColumn(b // 2)
    printRow()

printMessage(testString)
printMessage("Another message.", 2)
printMessage("Another message.", 3)
printMessage("Another message.", 4)
printMessage("Another message.", 5)

