#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:11:43 2017

@author: ratnadeepb
@License: MIT
@Version: 2017.1
"""

import subprocess
import sys
import os

def ping_ip(ip):
    if os.name == "posix":
        cmd = "ping -c 1 {} | grep -i '64 bytes'".format(ip)
    else:
        cmd = "ping -c 1 {} | findstr Reply".format(ip)
    
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    p.wait()
    if p.stdout.read():
        return True
    else:
        return False


if os.name == "posix":
    filename = "/etc/services"
else:
    filename = "C:Windows/System32/drivers/etc/services"
ports = []
with open(filename, "r") as services:
    for line in services.readlines():
        if line.find('tcp') > -1 or line.find('udp') > -1:
            ar = line.split()
            port = ar[1]
            ports.append(port)

def port_scan(ip, fileid):
    if os.name == "posix":
        cmd = "./port_scanner.sh {}".format(ip)
    else:
        cmd = "port_scanner.bat {}".format(ip)
    cmd_orig = cmd
    
    for port in ports:
            port = port[:-4]
            cmd = cmd_orig + " {}".format(port)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
            for item in iter(lambda: p.stdout.read(1), ''):
                sys.stdout.write(item)
                fileid.write(item)

    err = p.stderr.read()
    if err != '':
        sys.exit(err)