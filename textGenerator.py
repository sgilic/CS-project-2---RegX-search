#!/usr/bin/python -tt

import sys
import os
import string
import random

def main():
	f = open("longText.txt","w")
	for i in range(10000):	
		rand = ''
		rand += ''.join([random.choice(string.ascii_letters + string.digits) for n in range(60)])
		f.write(rand + '\r')
	f.close()

if __name__ == "__main__":
	main()
