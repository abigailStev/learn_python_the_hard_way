# This exercise is really cool

x = "There are %d types of people." % 10 # including in a variable?!
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # puts 'hilarious' in to the % in the variable joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

print w + e # concatenating strings

print