#!/usr/bin/python -tt

import sys
import os
import commands
import re
import time

def main():
	filename = os.path.abspath(sys.argv[1])
	pattern = sys.argv[2]
	#Enter nrgrep path
	cmd = "/home/sgilic/Gil/nrgrep-1.1.2/nrgrep"

	print ("NR-GRep :")
	print ("search pattern: " + pattern)
	print ("in file: " + filename)    
	
	status, output = commands.getstatusoutput(cmd+" "+pattern+" "+filename)
	results = re.finditer(pattern,str(output))

	for res in results:
		start_time = time.time()
		status, output = commands.getstatusoutput(cmd+" "+str(res.group())+" "+filename)	
		pos_str = '[' + str(res.start()) + ',' + str(res.end()) + ']'	
		end_time = time.time()
		print(res.group() + ', ' + pos_str + ', '+str((end_time - start_time)*1000))
	

if __name__ == "__main__":
    main()
