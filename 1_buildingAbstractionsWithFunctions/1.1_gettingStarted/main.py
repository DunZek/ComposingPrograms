from urllib.request import urlopen  # <- loading internet-comm. functionality by enabling a function that can access content via uniform resource locator

# Statements (actions which are carried out) & Expressions (computations which are evaluated) - that which Python code consists of where programs instruct to either:
#   1. Compute some value
#   2. Carry out some action
shakespeare = urlopen("http://composingprograms.com/shakespeare.txt")  # a statement

# Functions - encapsulators of data-manipulating logic (Featured in chapter 1, this chapter)
words = set(shakespeare.read().decode().split())  # furthermore statements but using more functions
# ^^ read data from URL, decode data into text, split text into words, put words into a set and assign it to "words" variable

# Objects - a complexity-management bundle of data and logic used to manipulate said data (Featured in chapter 2)
print( {w for w in words if len(w) == 6 and w[::-1] in words} )  # an expression - evalutes to the set of all words that are sinultaneously a word spelled in reverse
