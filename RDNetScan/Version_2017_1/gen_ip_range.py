#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:34:16 2017

@author: ratnadeepb
@License: MIT
@Version: 2017.1
"""

import sys
import re

def prep_ips(ip1, ip2):
    # Split the indovidual bytes
    pattern = re.compile('\.')
    arg1 = pattern.split(ip1)
    arg2 = pattern.split(ip2)
    
    # Check if the arguments are indeed IPs
    try:
        int(arg1[0])
    except ValueError:
        sys.exit("This program does not deal with hostnames")
    
    try:
        int(arg2[0])
    except ValueError:
        sys.exit("This program does not deal with hostnames")
    
    # There should be four bytes
    if len(arg1) != 4 or len(arg2) != 4:
        sys.exit("Incorrect IP")
    
    # The starting and ending bytes can't be less than 1
    # The middle bytes can't be less than 0
    # No byte can be larger than 254
    for pos, byte in enumerate(arg1):
        if pos == 0 or pos == 3:
            if int(byte) > 254 or int(byte) < 1:
                sys.exit("Incorrect IP")
        else:
            if int(byte) > 254 or int(byte) < 0:
                sys.exit("Incorrect IP")
    return [arg1, arg2]
    
# This function will generate the IPs
def ip_gen(ip1, ip2):
    for i in range(int(ip1[0]), int(ip2[0]) + 1):
        if i != int(ip2[0]):
            last = 254
        else:
            last = int(ip2[1])
        if i != int(ip1[0]):
            first = 0
        else:
            first = int(ip1[1])
        
        for j in range(first, last + 1):
            if j != int(ip2[1]):
                last = 254
            else:
                last = int(ip2[2])
            if j != int(ip1[1]):
                first = 0
            else:
                first = int(ip1[2])
                
            for k in range(first, last + 1):
                if k != int(ip2[2]):
                    last = 254
                else:
                    last = int(ip2[3])
                if k != int(ip1[2]):
                    first = 1  # The last byte has to be a host ID
                else:
                    first = int(ip1[3])
                
                for l in range(first, last + 1):
                    yield str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l)