#!/usr/bin/env python

import urllib2
import re
import sys

response = urllib2.urlopen('http://10.9.16.15/phone_dumps/all.txt')

for line in response:
	if "Oliver Gross" in line:
		olidata = line

olilist = olidata.split("\t")

if olilist[5] != "AVIL":
	print "GET ON THE PHONE DUMASS"
else:
	print "Nice work, doofus."



#print(olilist[5])






#rawdata = response.read()

#justoli = re.findall (".*", rawdata)

#print(justoli)

#for line in rawdata:#
#	if "Oliver" in line
#		print(line)
