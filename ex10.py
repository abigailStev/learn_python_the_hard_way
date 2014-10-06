tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

bonus_cat = """ More things
for me to type!
I am so excited """

bonus_kitten = ''' More things
for me to type!
I am so excited '''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat # notice how this one has blank lines at the beginning and end
print bonus_cat # and this one doesn't, because of where the """ are placed
# however, bonus_cat does have a space at the beginning when printed
print bonus_kitten # seems to do the same thing as bonus_cat

print 


a = 0
while a < 50:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i
		a = a + 1
		
print