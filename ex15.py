from sys import argv

script, filename = argv
# you always need to tell it to read in the script name, since that's always the 
# first argument!

# run 'pydoc file' (no quotes) in the cmd line to learn what you can do to files

txt = open(filename)
# this doesn't return the contents of the file
# it makes a file object and allows it to be used for reading or writing

print "Here's your file %r:" % filename
print txt.read() # this line reads in the file contents and prints them

print "Type the filename again:"
file_again = raw_input(" >> ")

txt_again = open(file_again) #again, need to open a file before we can read its contents

print txt_again.read()

txt.close()
txt_again.close()
# it's important to close files after opening them

## you can also open and read files straight from the python command line. don't forget
## to close them though

# Python doesn't restrict you from opening a file more than once, but be careful with it!