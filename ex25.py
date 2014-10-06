def break_words(stuff):
	"""This function will break up words for us."""
	# the above line is a documentation comment. these are useful!!
	# they appear when you type help(ex25) within python in terminal
	# or help(ex25.break_words)
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	# pop takes the word off the list, and removes it for use
	print word 

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	# pop takes the word off the list, and removes it for use
	print word 

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# the study drills here: http://learnpythonthehardway.org/book/ex25.html
# show how to use this. from ex25 import * is the most useful one! (within python)
