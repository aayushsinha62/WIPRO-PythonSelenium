#match - returns the exact sequence

import re #re-regular expression

#o/p is match object - matched sequence and span() - start and end index

#match only check at the starting of the string

text="hello world"
result=re.match("hello",text)
print(result)

#using pattern

test_str="1232232dfdfdghdfd"
pattern=re.compile("df") #case-sensitive
matches=pattern.finditer(test_str)

for match in matches:
    print(pattern)


#finditer() finds all the non-overlapping matches of a pattern in a string and
#returns an iterator of match objects (not a list)

#findall - finds all string there the re matches and returns a list



#search operation #searches entire string
#returns the first occurence

text="python is powerful among all powerfuls"
result=re.search("powerful",text)
print(result)

#search - searches entire string - find occurence - returns first occurence
#match - searches beginning string only and returns that - used to validate formats

#raw string r

a=r"\tHello"
print(a)


my_string="abc1232323AB432123abc"
pattern=re.compile(r'123')
matches=pattern.findall(my_string)

for match in matches:
    print(match)

# modification methods
# match ()- Determine If the RE matches at the beginning of the string,
# search ( ) -Scan through o string, looking for any location where this RE matches.
# finditer()- Find all substrings where the RE matches, and returns then as an Iterator.
# findall() - find all the strings where the re matches and returns a list


#methods on match

# group()- Return the string matched by the RE
# start(): Return the starting position of the natch
# send(): Return the ending position of the •atch
# span(): Return a tuple containing the (start, end) positions of the match

test_string="123sdjsdjsdds343434abc12345"
pattern=re.compile(r'abc')
matches=pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(),match.start(),match.end())
    print(match.group()) #return the substring that was matched by the RE

#special characters
#meta character
#regular expression

#Pattern Matching

#abc matches exact test
#match exact "abc" where ever it is appearing

text="I like abc and abcde"
result=re.findall("abc",text)
print(result)

#[abc] a or b or c - matches any one of the character
#matches single characters : a OR b OR c
text="apple banana cat"
result=re.findall("[abc]",text)
print(result)

#[a-z] lowercase letters
text="I like abc and ABCDEFGH"
result=re.findall("[a-z]",text)
print(result)

#[0-9] digits
text="I like abc and 123232ABCDEFGH"
result=re.findall("[0-9]",text)
print(result)


#a or b
text="cat bat rat mat"
result=re.findall("cat|bat",text)
print(result)
#matches either cat or bat

#any single character
text="cat bat rat bob"
result=re.findall("c.t",text)
print(result)


#special characters

# special sequences begin with a backslash \
# sequence meaning example

# Special sequences begin with a backslash \.
# Sequence    Meaning    Example
# \d  Digit (0–9)    \d\d
# \D  Non-digit  \D
# \w  Word char (a-z, A-Z, 0-9, _)   \w+
# \W  Non-word char  \W
# \s  Whitespace \s
# \S  Non-whitespace \S
# \b  Word boundary  \bcat\b
# \B  Not a word boundary    \Bcat


# \d  Digit (0–9)    \d\d

print(re.findall(r"\d","Order 123 costs 450"))

# \D  Non-digit  \D

print(re.findall(r"\D","Order 123 costs 450"))

# \w  Word char (a-z, A-Z, 0-9, _)   \w
text="Python_3 version!"
print(re.findall(r"\w",text))

# \W  Non-word char  \W
text="hello@123"
print(re.findall(r"\W",text))

# \s  Whitespace \s

text="Hello world\nPython"
print(re.findall(r"\s",text))

# \S  Non-whitespace \S

text="Hi there"
print(re.findall(r"\S",text))

# \b  Word boundary  \bcat\b

text="cat scatter catalog"
print(re.findall(r"\bcat\b",text))


#matches only full word "cat"
# \B  Not a word boundary    cat\Bc
text="cat scatter catalog"
print(re.findall(r"cat\B",text))

#meta characters

#^start of the string

text="Python is easy"
print(re.findall(r"^Python",text))

# Meta - characters
# have
# special
# meaning in regex.
#
# Meta - character
# Meaning
# .Any
# character
# ^ Start
# of
# string
# $   End
# of
# string
# *0 or more
# +   1 or more
# ?   0 or 1
# {n}
# Exactly
# n
# times
# {n, }
# n or more
# {n, m}
# Between
# n and m
# []
# Character
# set
# ()
# Grouping
# '''

#^ Start of string
text="Python is easy"
print(re.findall(r"^Python",text))

#$ end of string
text="Python is easy"
print(re.findall(r"easy$",text))

#* 0 or more
text="ab abb abbb a n"
print(re.findall(r"ab*",text))

#+ 1 or more
text="ab abb abbb a"
print(re.findall(r"ab+",text))

#? 0 or 1
text="color colour colr"
print(re.findall(r"colou?r",text))

#{n} Exactly n times
text="111 22 3333 68777"
print(re.findall(r"\d{3}",text))

#{n,} n or more
text="1 22 333 444"
print(re.findall(r"\d{3,}",text))

#{n,m} between n and m
text="111 22 3333 68777"
print(re.findall(r"\d{3,4}",text))

#[] character set

text="apple banana cat"
print(re.findall(r"[abc]",text))

#() Grouping
text="2026-02-22"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",text))





