#!/bin/python3

# Functions

from datetime import date

#Write your function here!
def get_todays_date():
    return date.today()

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())
print(str(str(get_todays_date()).replace("-","/")))

def efficientDate():
    return str(date.today()).replace("-","/")

print(efficientDate())
