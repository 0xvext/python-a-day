#!/bin/python3

# Functions

from datetime import date

def get_todays_date():
    return date.today()

print(get_todays_date())
print(str(str(get_todays_date()).replace("-","/")))

def efficientDate():
    return str(date.today()).replace("-","/")

print(efficientDate())
