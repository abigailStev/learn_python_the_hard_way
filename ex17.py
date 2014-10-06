from sys import argv
from os.path import exists # lets you find out if a file already exists or not

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

# can also write indata = open(from_file).read()   and then don't need to close it

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "All done"

out_file.close()
in_file.close()
# probably good practice to close things in opposite order you opened them, like brackets
