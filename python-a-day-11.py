#!/bin/python3

# Loops and indices 

for i in range(5, 9):
    print("Index", i)

myString = "A string of letters."
for i in range(0, len(myString)):
    print(i, myString[i])

myList = ["This", "is", "a", "list", "of", "words"]
for i in range(0, len(myList)):
    print(i, myList[i])

# For-each loop:

myString = "This is a string"
index = 0

for i in myString:
    print(index, i)
    index += 1

# While loop:

myValue = 64

while myValue <= 100:
    myValue += 5
    print(myValue)

# Nested while loops

myInt_1 = 5
myInt_2 = 6
myInt_3 = 8

while myInt_1 > 0:
    while myInt_2 > 0:
        while myInt_3 > 0:
            myInt_1 -= 1
            myInt_2 -= 1
            myInt_3 -= 1
            print(myInt_1, myInt_2, myInt_3)  

#    continue: Skip the rest of the current iteration of the loop and continue with the next iteration of the loop (if there is a next iteration).
#    break: Skip the rest of the current iteration of the loop and break out of the loop altogether, skipping any later iterations, too.
#    pass: Designate an 'empty' body for a control structure.



