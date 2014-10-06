days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# \n is newline, \t is tab
# newline doesn't work when you print the variable using newline in %r format, only %s format

print "Here are the days: ", days
print "Here are the months: \n", months

print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # cannot have spaces between the three double quotes for it to work like this
# single quotes works the same as double quotes in the above example (see ex 10)