#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test2.py
#  
#  Copyright 2015 Andy <Andy@ANDY-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

NUM_ARGUMENTS = 5
slash = "\\"
from sys import argv
from os import system
from os import getcwd
from string import *

arguments = {}


print "Num of arguments passed:",len(argv) -1

if len(argv)-1 != NUM_ARGUMENTS*2:
	print "ERROR: You must pass only",NUM_ARGUMENTS*2,"arguments!"
	exit(0)

i = 1
while i < len(argv):
	print "!"
	if argv[i].find("-") != -1:
		arguments[argv[i][1:]] = argv[i+1]
		i = i + 1
	i = i + 1
print arguments
print "working directory:",getcwd()

arguments_names = ["inputDWIVolume", "atlas", "atlast1", "atlast2", "M"]

for k in arguments.keys():
	if not (k in arguments_names):
		print "ERROR:", k, "is not a valid paramater!"
		exit(0)

for k in arguments.keys():
	if arguments[k][0] == '-':
		print "ERROR:",arguments[k], "is not a valid parameter value for", k
		exit(0)
	if arguments[k].find(slash) == -1:				
		arguments[k] = getcwd() + slash + arguments[k] 
	
#all arguments were checked

#running dtiestim
outputDTIName = arguments["inputDWIVolume"]
if outputDTIName.find("DWI") != -1:
	outputDTIName = outputDTIName.replace("DWI", "DTI")
else:
	outputDTIName = outputDTIName.split(".")[0] + "_DTI" + "." + outputDTIName.split(".")[1]
	
system("dtiestim -M "+arguments["M"]+" -m wls --correctionType nearest --inputDWIVolume "+arguments["inputDWIVolume"]+" --outputDTIVolume "+outputDTIName)	


#running dtiprocess
outputMDName = outputDTIName.replace("DTI", "MD")
outputADName = outputDTIName.replace("DTI", "AD")
outputRDName = outputDTIName.replace("DTI", "RD")
system("dtiprocess --dti_image "+outputDTIName+" -m "+outputMDName+" --lambda1_output "+outputADName+" --RD_output "+outputRDName)



