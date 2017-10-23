Author="Ratnadeep Bhattacharya"
License="MIT"
VERSION="2017.1"
chmod u+x port_scanner.sh
clear

echo Author:  $Author
echo License: $License
echo Version: $VERSION
echo Usage:   We just need a starting and ending IP and we will scan all ports
echo          for all IPs between these two IPs.
echo Any weird looking errors are mostly caused by:
echo "	1. Python 2.7 being not available"
echo "	2. ICMP being blocked by firewall"
echo "Do you need more help?(yes/no)"
read ans

if [ "$ans" == "yes" ]
then
	echo Please read the README for more detail
	exit
fi

echo "Please enter the starting IP address:	"
read start
echo "Please enter the ending IP address:	"
read end
echo "Please enter the path where you want to store the report."
echo "This is optional"
read path

echo Starting the scanner
if [ "$path" == "" ]
then
	echo No Path provided
	python network_scanner.py $start $end
else
	echo Report will be stored at $path
	python network_scanner.py $start $end $path
fi

echo End of Script
