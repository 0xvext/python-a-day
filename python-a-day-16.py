#!/bin/python3

# Outputting message boxes of varying height

import os

# Get the terminal size and store into list (0 = rows, 1 = columns)
dimensions = [int(n) for n in os.popen('stty size', 'r').read().split()]

# Message to print
testString = "This is a message, 0."

# Reduce width by 1 if odd
if dimensions[1] % 2 != 0:
    dimensions[1] -= 1

# Print a single # with no line break
def printHash():
    print("#", end="")

# Print blank space before the message
def printBufferBefore(a):
    if len(a) < dimensions[1]:
        for i in range((dimensions[1] - 2 - len(a)) // 2):
            print(" ", end="")

# Print blank space after the message
def printBufferAfter(a):
    if len(a) < dimensions[1]:
        for i in range((dimensions[1] - 2 - len(a)) // 2):
            print(" ", end="")
        if (dimensions[1] - 2 - len(a)) % 2 != 0:
            print(" ", end="")

# Print vertical # to height of box
def printColumn(height):   
    # If height of box is an even number, add 1
    if height % 2 == 0:
        height += 1

    for i in range(height):
       printHash()
       for i in range(int(dimensions[1]) - 2):
           print(" ", end="")
       printHash()
       print()

# Print a row of # to fill width
def printRow():
    for i in range(int(dimensions[1])):
        print("#", end="")
    print()

def printMessage(a):
    print(a, end="")

# Draw a box with the message inside
def messageBox(a, b = 0):
    printRow()
    printColumn(b // 2)
    printHash()
    printBufferBefore(a)
    printMessage(a)
    printBufferAfter(a)
    printHash()
    print()
    printColumn(b // 2)
    printRow()

messageBox(testString)
messageBox("Another message, 2.", 2)
messageBox("Yet another message, 3.", 3)
messageBox("Another message, still, 4.", 4)
messageBox("A much longer message that might wrap lines to see what happens, 5.", 5)

