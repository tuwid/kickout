#!/usr/bin/python

import subprocess
import argparse
import signal
import re
import os
import sys
# first we get the list of active users in ttys 
# then we let the user decide which user to kick out

# this is my first python script that i wrote on my own, 
# i'm a perl programmer and just want to learn python better 

# this program is free as in free air 

def check_if_root():
	if not os.geteuid() == 0:
		sys.exit('Script must be run as root')
	else:
		print "Root check OK"

def logged_users():
	who_output = subprocess.check_output("who").split("\n")
	myLoggedUsers = {}

	for line in who_output:
		#print line
		myList = re.match( r"(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)", line,re.I)
		if myList and myList.group(5):
			print myList.group(1), myList.group(2), myList.group(3),myList.group(4),myList.group(5)
			myLoggedUsers[myList.group(2)] = myList.group(1) 
		else:
			print ""
	if (len (myLoggedUsers) <= 0):
		sys.exit("No one logged in the system.. Exiting ")
	return myLoggedUsers

def kill_tty(tty):
		#sys.exit("\n Something wrong was typed")
		if tty in logged_users():
			print "tty found"
		else:
			print "tty not found"
			sys.exit(1)

		out = subprocess.check_output(['ps', 'aux'])
		for line in out.splitlines():
			if tty in line:
				#print line
				pid = int(re.match( r"^(\S*)\s*(\S*)", line,re.I).group(2))
				try:
					os.kill(pid, signal.SIGKILL)
				except:
					print ""
				print "tty " + tty + " killed"
		else:
			print ""
			#print "tty not found running"


parser = argparse.ArgumentParser(description='''script to kick/logout users out of a linux system ./kick.py -k pts/6''')
parser.add_argument("-l", '--list', help='list users and ttys', action="store_true")
parser.add_argument("-k", '--kill', metavar="tty", type=str, help="kill user in specified tty")
args = parser.parse_args()

#print args.kill
if (args.kill == None and args.list == False):
	parser.print_help()

if args.list:
	logged_users()
elif args.kill:
	check_if_root()
	kill_tty(args.kill)



