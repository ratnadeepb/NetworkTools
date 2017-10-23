@echo off
Author="Ratnadeep Bhattacharya"
License="MIT"
VERSION="2017.1"
cls

echo Author:  $Author
echo License: $License
echo Version: $VERSION
echo Usage:   We just need a starting and ending IP and we will scan all ports
echo          for all IPs between these two IPs.
echo Any weird looking errors are mostly caused by:
echo 	1. Python 2.7 being not available
echo 	2. ICMP being blocked by firewall
set /P ans=Do you need more help?(yes/no)	

if %ans%=="yes" (goto :exit_loop) else (goto :normal)
:exit_loop
	echo Please read the README file for more details
	pause
	exit

:normal
set /P start=Please enter the starting IP address:	
set /P end=Please enter the ending IP address:	
echo Please enter the path where you want to store the report.
set /P path=This is optional:	

echo Starting the scanner

if "$path" == "" (goto :no_path) else (goto :path_exists)
:no_path
	echo No Path provided
	python network_scanner.py %start% %end%

:path_exists
	echo Report will be stored at %path%
	python network_scanner.py %start% %end% %path%

echo End of Script
