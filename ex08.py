formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # closing both parentheses is important!!
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) # Boolean values must be Capitalized
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you couldn't type up right.",
	"But it didn't sing.",
	"So I said goodnight."
) # note the indents and the commas -- both are important
# indents must be TAB, not spaces

print 