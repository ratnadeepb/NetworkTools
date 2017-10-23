#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:40:13 2017

@author: ratnadeepb
@License: MIT
@Version: 2017.1
"""

from gen_ip_range import prep_ips, ip_gen
from find_ip_ports import ping_ip, port_scan

import sys

def network_scanner(ip1, ip2, filename):
    arg1, arg2 = prep_ips(ip1, ip2)
    
    ips = ip_gen(arg1, arg2)
    try:  # If user provided file does not exist and cannot be created
        with open(filename, "w") as scan:
            while True:
                try:
                    cur_ip = ips.next()
                    print "Checking IP: " + cur_ip
                except StopIteration:
                    break
                if ping_ip(cur_ip):
                    print cur_ip + " is alive"
                    print "Checking for open ports"
                    scan.write(cur_ip)
                    scan.write('\n')
                    port_scan(cur_ip, scan)
    except IOError as e:
        print e
    print "Result stored in {}".format(filename)
                
if __name__ == "__main__":
    import os
    if len(sys.argv) < 3:
        sys.exit("Usage: python network_script.py <starting_ip> <ending_ip>")
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        sys.exit("Usage: python network_script.py <starting_ip> <ending_ip>")
    else:
        try:
            filename = sys.argv[3] + "scanner_report.txt"
        except IndexError:
            if os.name == 'posix':
                filename = "/tmp/scanner_report.txt"
            else:
                filename = "scanner_report.txt"
                
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        network_scanner(arg1, arg2, filename)
