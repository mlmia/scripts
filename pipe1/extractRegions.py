__author__ = 'JESSEROCHA'

import sys
import os

#Checking number of arguments
if len(sys.argv)-1 != 2:
	print "ERROR: this script needs 2 parameters, example:"
	print "'extractRegions.py -config configRegions.txt'"
	exit(-1)
else:
	print "Number of arguments: ", len(sys.argv)-1

#Checking if the input is  correct:
if (sys.argv[1] != "-config"):
	print "ERROR: unable to find the input file."
	print "Type, for example,'extractRegions.py -config configRegions.txt'"
	exit(-1)
else:
	print "Input file was found"

var_file = open(sys.argv[2],"r")

lines = var_file.readlines()

if len(lines) != 3:
	print "ERROR: the configuration file must have 3 lines. Please check the example below:"
	print "input image:/home/workstation1/test_scripts/Atlaswarp/warped_brain.nrrd"
	print "output image:/home/workstation1/test_scripts/Atlaswarp/region1.nii.gz"
	print "extract label:1"
	exit(-1)


else:
	print "File Checked! It has 3 lines."


NAME_ARGS = []

#getting the location
for i in range(len(lines)):
 split_str = lines[i].rstrip().split(':')
 NAME_ARGS.append(split_str[1])


#running ImageMath
os.system("ImageMath " + NAME_ARGS[0] + " -extractLabel " + NAME_ARGS[2] + " -outfile " + NAME_ARGS[1] )

print "done!!!!!!!!"

var_file.close()