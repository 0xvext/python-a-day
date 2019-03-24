#!/bin/python3

# More functions

def snowed_in(temperature, weather, is_celsius=True):
    if weather == "snowy":
        return True
    if is_celsius==True:
        if temperature <= 0:
            return True
        else:
            return False
    elif temperature <= 32:
            return True

print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True
