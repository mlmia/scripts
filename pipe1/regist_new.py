#!/usr/bin/env python
# -*- coding: utf-8 -*-

#NUM_ARGUMENTS = 1
#slash = "/"
import sys
import os
arguments = {}


arguments_names = ["-config","config_regist.txt","RD","T1","T2","ATLAS","OUT_ANTS_PREFIX"]

arguments[sys.argv[1][1:]]=sys.argv[2]

arguments["config"]

#Checking number of arguments
if len(sys.argv)-1 != 2:
	print "ERROR: this script only needs 2 parameters, example:"
	print "'regist_new.py -config config_regist.txt'"
	exit(0)
else:
	print "Number of arguments: ", len(sys.argv)-1


#Checking if the input is  correct:
if (sys.argv[1] != arguments_names[0]) or (sys.argv[2] != arguments_names[1]):
	print "ERROR: unable to find the input file."
	print "Please type: regist_new.py -config config_regist.txt"
	exit(0)
else:
	print "input file was found"


f  = open(arguments["config"])
lines = f.readlines()


if len(lines) != 6:
	print "ERROR: the configuration file must have only 6 lines. Please check the example below:"
	print "RD:/file location"
	print "T1:/file location"
	print "T1:/file location"
	print "ATLAS:/file location"

else:
	print "the file was read and has 6 lines"


ID_ARGS = []
NAME_ARGS = []


for i in range(0,len(lines)):
	#arguments[arguments_names[i+2]] = lines[i]
	#arguments[arguments_names[i+2]]=lines[i].split(':')
	#print arguments[i]

	split_str = lines[i].rstrip().split(':')
	ID_ARGS.append(split_str[0])
	NAME_ARGS.append(split_str[1])


#running ANTS
os.system("ANTS 3 -m CC\["+NAME_ARGS[0]+","+NAME_ARGS[1]+",1,4\] -m CC\["+NAME_ARGS[0]+","+NAME_ARGS[2]+",1,4\] -r Guass\[3,0\] -i 100x50x25 -t SyN\[0.25\] -o "+NAME_ARGS[4])



#running WARP
os.system("WarpImageMultiTransform 3 "+NAME_ARGS[3]+" "+NAME_ARGS[5]+" -R "+NAME_ARGS[0]+" --use-NN "+NAME_ARGS[4]+"Warp.nii.gz"+" "+NAME_ARGS[4]+"Affine.txt")


 



print "done!!!!!!!!"



