# Write a regex to check if a string contains only digits.
import re

s1="123456"
print(re.fullmatch(r'\d+',s1))

# Write a pattern to match a 10-digit mobile number.

s2="9867232232"
print(re.fullmatch(r'\d{10}',s2))

# Find all lowercase letters in a string.

s3="Python"
print(re.findall(r'[a-z]',s3))

# Extract all uppercase letters from a sentence.

s4="hello WORLD"
print(re.findall(r'[A-Z]',s4))

# Match a string that starts with "Hello"

s5="Hello World"
print(re.match(r'^Hello',s5))

# Match a string that ends with "world".

s6="Hello World"
print(re.search(r'World$',s6))

# Find all words separated by spaces.

s7="Hello World I am Here"
print(re.findall(r'\w+',s7))

# Match exactly 5 characters.

s8="Hello"
print(re.fullmatch(r'.{5}',s8))

# Find all occurrences of the word "python" (case-sensitive).

s9="python is fun, Python is powerful, python rocks"
print(re.findall(r'python',s9))

# Replace all spaces in a string with underscores.

s10="regex is very easy"
print(re.sub(r'\s','_',s10))

#regular expression modifiers

'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''

#regular expression modifiers
#re.IGNORECASE re.I Case_insensitive matching
text="Python"
print(re.search("python",text,re.I))
#re.MULTILINE re.M ^and$ match each line
text="Hello\nPython"
print(re.search("^Python",text,re.M))
#re.DOTALL re.s matches newline
text="Hello\nWorld"
print(re.search("Hello.*World",text,re.S))
#re.VERBOSE re.X write readable regx with comments - make it more readable
pattern=re.compile(r"""7879hbgjklksdgdskl..^^&*&89""",re.X)
print(pattern)
#re.ASCII re.A ASCII-only matching
print(re.findall(r'\w+',text,re.A))
#re.DEBUG - Debug pattern
pattern=re.compile(r"""7879hbgjklksdgdskl..^^&*&89""",re.DEBUG)
print(pattern)


#assertions

# ^ → Start of string
# $ → End of string
# \b → Word boundary
# \B → Not word boundary
# (?=...) → Positive Lookahead
# (?!...) → Negative Lookahead
# (?<=...) → Positive Lookbehind
# (?<!...) → Negative Lookbehind

# (?=...) → Positive Lookahead
text="user1 admin2 test"
print(re.findall(r"\w+(?=\d)",text))

# (?!...) → Negative Lookahead
text="user1 admin test2"
print(re.findall(r"\w+(?!\d)",text))

# (?<=...) → Positive Lookbehind
text="Price a500"
print(re.findall(r"\w+(?<=a)d+",text))

# (?<!...) → Negative Lookbehind
text="a500 300"
print(re.findall(r"\w+(?<!a)\d+",text))

