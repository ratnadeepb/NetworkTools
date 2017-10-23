#!/bin/bash
# Find open ports in a remote server
# Author: ratnadeep.bhattacharya1983@gmail.com
# Version: 2017.1

nc -zv $1 $2 > /dev/null 2>&1
if [ $? == 0 ]
then
	echo $2
fi
