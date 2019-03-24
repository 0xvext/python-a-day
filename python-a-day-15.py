#!/bin/python3

# More functions
# Requires netifaces library: pip3 install netifaces
# Flaws: statically assumes ens33 interface; lists MAC, IPv4 and IPv6

import netifaces

# Define func
def getMyAddress():
    # Create a variable to pull from ens33 interface
    myAddress = netifaces.ifaddresses('ens33')
    # Loop through items in resulting list
    for i in myAddress:
        # Loop through items in resulting dict
        for j in myAddress[i]:
            # Print the 'addr' element of each dict
            print(j['addr'])
# Call fun
getMyAddress()
