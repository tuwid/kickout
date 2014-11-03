#!/usr/bin/python

import subprocess
import signal
import re
import os
import sys

# first we get the list of active users in ttys 
# then we let the user decide which user to kick out

# this is my first python script that i wrote on my own, 
# i'm a perl programmer and just want to learn python better 

# this program is free as in free air 

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

who_output = subprocess.check_output("who").split("\n")

myList = []
myLoggedUsers = {}
nr = 1;

for line in who_output:
	#print line
	list = re.match( r"(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)", line,re.I)
	if list and list.group(5):
	   print nr, " - ",list.group(1), list.group(2), list.group(3),list.group(4),list.group(5)
	   myLoggedUsers[nr] = list.group(2)
	   nr+=1
	else:
	   print ""

if (len (myLoggedUsers) <= 0):
	sys.exit("No one logged in the system.. Exiting ")

try:
	choice = int(raw_input("Please enter id of the user to kick : "))
except:
	sys.exit("\n Something wrong was typed")

if (int(choice) > 0 and int(choice) < nr):
	out = subprocess.check_output(['ps', 'aux'])
	for line in out.splitlines():
		if myLoggedUsers[choice] in line:
			#print line
			pid = int(re.match( r"^(\S*)\s*(\S*)", line,re.I).group(2))
			os.kill(pid, signal.SIGKILL)
			print "tty " + myLoggedUsers[choice] + " killed"
else:
	print "Entry out of id range"
