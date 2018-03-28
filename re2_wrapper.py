#!/usr/bin/python -tt

import sys
import os
import commands
import re2
import time

def getResMatch (res):
	return str((str(res)).split("\'")[1])

def main():
	filename = os.path.abspath(sys.argv[1])	
	pattern = sys.argv[2]
	with open(filename) as tmp:
    		data = tmp.read()
	print ("RE-2 :")
	print ("search pattern: " + pattern)
	print ("in file: " + filename)    
	
	results = re2.finditer(pattern, data)
	
	for res in results:		
		start_time = time.time()	
		match = re2.search(getResMatch(res),data)
		end_time = time.time()
		pos_str = '[' + str(res.span()[0]) + ',' + str(res.span()[1]-1) + ']'
		print(getResMatch(res) + ', ' + pos_str + ', ' + str((end_time - start_time)*1000))

if __name__ == "__main__":
    main()
