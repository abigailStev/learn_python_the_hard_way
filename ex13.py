import sys
# things we import are called modules or libraries
from sys import argv
# argv is the argument variable, for reading in arguments from the command line

script, first, second, third = argv
#int(third)   # forces third to be an integer, since argv is automatically a string

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

hi = raw_input("Say something: ")
print "You said \"%s\"" % hi # \" prints a "

# to run this program, type: python ex13.py a b c
# it prints: 
# The script is called:  ex13.py
# Your first variable is:  a
# Your second variable is:  b
# Your third variable is:  c

# argv lets you specify variables as you call the script
# input forces the user to interact with the script as it runs

#argv come in as strings, but you can force them to other types like int() just like with raw_input
# see commented out example above