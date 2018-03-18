# CS-project-2---RegX-search

This folder contains the following files:

1. guidelines.txt

Contains project's spesifications.

2. textGenerator.py

python script that generates random text file (60 chars per line * 10K lines)
file name is longtext located at the script's directory.
               
-- the script can be configurated easily according to requierment.

3. longText.txt

textGenerator.py sample output.

4. simple.txt

basic text file for checking output.

5. nr-grep_wrapper.py

nr-grep activation:

      a) change nr-grep installation path at the lines 13 (e.g "/home/sgilic/Gil/nrgrep-1.1.2/nrgrep")
      
      b) in command line:
      
            python <path to nr-grep_wrapper.py>/nr-grep_wrapper.py <filename (where we search for pattern)> <pattern>

6. re2_wrapper.py

re2 activation:

        
              ./<path to re2_wrapper.py>/re2_wrapper.py <filename (where we search for pattern)> <pattern>

--------------------------------------------------------------------------------------------------------------------

# Installations

nr-grep:

      1. copy files from:
      
            https://www.dcc.uchile.cl/~gnavarro/software/nrgrep.tar.gz
            
      2. run "make", which will produce the executable "nrgrep".
      
re2:

      1. git clone https://code.googlesource.com/re2
      
      2. cd re2
      
      3. make
      
      4. make test
      
      5. make install
      
      6. make testinstall
      
      7. git clone git://github.com/axiak/pyre2
      
      8. cd pyre2.git
      
      9. sudo python setup.py install
      
-- for more information:

  https://pypi.python.org/pypi/re2/0.2.20
  
 --------------------------------------------------------------------------------------------------------------------

# Documentation

nr-grep:
      https://www.dcc.uchile.cl/~gnavarro/ps/spe01.pdf
      
re2:
      https://github.com/google/re2/wiki

 --------------------------------------------------------------------------------------------------------------------

# Notes

nr-grep delivers search results simultaneously.
In order to distinguish between results search time, nr-grep_wrapper.py uses pre-processing stage
for collecting the results and messures each result search time separately.


   
