#!/bin/python3

# More functions
# Requires netifaces library: pip3 install netifaces
# Flaws: statically assumes ens33 interface; lists MAC, IPv4 and IPv6

import netifaces

def getMyAddress():
    myAddress = netifaces.ifaddresses('ens33')
    for i in myAddress:
        for j in myAddress[i]:
            print(j['addr'])

getMyAddress()
