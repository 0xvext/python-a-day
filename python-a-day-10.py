#!/bin/python3

# Do more with loops and ifs 

for i in range(10):
    print(i + 1)

for i in range(-5, 6, 1):
    print(i)

for i in range(1, 20, 2):
    print(i + 1)

some_int = 5
sum = 1

for i in range(1, some_int + 1):
    sum *= i

print(sum)
