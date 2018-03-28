#!/usr/bin/python -tt

import sys
import os
import commands
import re
import time
import mmap

def getLenAndIter(iterator):
	temp = list(iterator)
	return len(temp), iter(temp)

def main():
	filename = os.path.abspath(sys.argv[1])
        f = open(filename, 'r+b')
	mf = mmap.mmap(f.fileno(), 0)
	mf.seek(0)
	pattern = sys.argv[2]
	#Enter nrgrep path
	cmd = "/home/sgilic/Gil/nrgrep-1.1.2/nrgrep"

	print ("NR-GRep :")
	print ("search pattern: " + pattern)
	print ("in file: " + filename)    
	
	status, output = commands.getstatusoutput(cmd+" "+pattern+" "+filename)
	results = re.finditer(pattern,str(output))
	len_results, results = getLenAndIter(results)
	for res in results:
		start_time = time.time()
		status, output = commands.getstatusoutput(cmd+" "+str(res.group())+" "+filename)
		match = res.group()
		if len_results > 1:
			match_loc = res
		else:
			match_loc = re.search(match, mf)	
		mf.seek(1,1)	
		pos_str = '[' + str(match_loc.start()) + ',' + str(match_loc.end()-1) + ']'	
		end_time = time.time()
		print (res.group() + ', ' + pos_str + ', '+str((end_time - start_time)*1000))
	
	mf.close()
	f.close()
	

if __name__ == "__main__":
    main()
