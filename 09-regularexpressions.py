###############################################################################
###
###   PYTHON 3: FROM IMPERATIVE TO OBJECT-ORIENTED TO FUNCTIONAL PROGRAMMING
###
###   Copyright Michel Pasquier, 2013-2018
###
###   This tutorial is meant to be used in class, interactively. By design,
###   it lacks the detailed explanations which are given by the instructor.
###   For these, and much more, see the many references provided throughout
###   these files as well as on the course site.
###



################################
##
##  TABLE OF CONTENT
##
##  01. Introduction to Python
##  02. Sequences and Collections
##  03. Flow Control and Repetition
##  04. Functions and Lambda Expressions
##  05. Classes and Inheritance
##  06. Exceptions and File I/O
##  07. Higher-Order Functions and Comprehensions
##  08. Iterators/Generators and Lazy Data Types
##  09. Regular Expressions and Pattern Matching: power of regex, syntax and
##              metacharacters, compiling patterns, functions, applications
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##



###############################################################################
###
###   09. REGULAR EXPRESSIONS
###



################################
##
##  THE POWER OF REGEX
##


# Very powerful pattern matching tool! e.g., in text editors, incl. IDLE(!)
# Example: searching for "using" in these tutorial files will give all 60+
# matches. How to find lines that contains "using" followed by "expression"
# and only those? This is a pattern! "using.*expression" -> 11 matches.
#
# Note that the pattern "reg.*exp" greedily matches anything that includes
# this pattern, incl. "regexp" and "regular expression", while the pattern
# "[a-z][0-9]" matches any lowercase letter followed by a digit, etc.
#
# Simplified regex are used everywhere(!) e.g., in Google search, Excel...
#import webbrowser
#webbrowser.open('https://support.google.com/websearch/answer/2466433')
#webbrowser.open('http://www.excel-easy.com/examples/find-vs-search.html')


# Regex module
import re

# Example: the goal is to abbreviate 'ROAD'as 'RD.' in a street address
# yes, string functions can be used... but only so far e.g.
adr = '100 NORTH MAIN ROAD, LONDON NW1, UK'
adr.replace('ROAD', 'RD.')          # works fine

adr = '100 NORTH BROAD ROAD, LONDON NW1, UK'
adr.replace('ROAD', 'RD.')          # oops!

adr.replace('ROAD,', 'RD.,')        # OK, but what if . or ; instead of , ?

# We need to use patterns! find and return matches, perform substitutions

re.sub('ROAD([.,;!])', 'RD.\\1', adr) # matches any punctuation!

re.sub('\bROAD\b', 'RD.', adr)      # matches ROAD when it's a word by itsef

re.sub('[.,;!?:]', '', 'Hello? cheers, uh? bye.') # strip any punctuation


# search(), findall(), match() take 2 args: a search pattern and a string;
# sub() take 3 args: a search pattern, a replacement pattern, and a string.

# note: all characters appearing in a regex match literally, unless they are
#       meta-characters or part of a pattern expression.



################################
##
##  METACHARACTERS AND SYNTAX
##


# [ ] specify a character class e.g., find all 'a', 'e', 'i', 'o' and 'u'
re.findall('[aeiou]', 'which foot or hand fell fastest')

# also by range e.g., find all chars from 'a' to 'd'
re.findall('[a-d]', 'which foot or hand fell fastest')

# ^ means negation (within brackets) e.g., find all chars except 'e' to 'z'
re.findall('[^e-z]', 'which foot or hand fell fastest')
re.findall('[^e-z] ', 'which foot or hand fell fastest')

# | matches either of the given alternatives e.g.
re.findall('ha|st', 'which foot or hand fell fastest')
re.findall('(cat|dog)s', '1 cat, 2 dogs, 3 more cats, 1 extra dog')

re.findall('a|e|i|o|u', 'which foot or hand fell fastest') # use [ ] better


# . matches anything except a newline character (use rregular expe.DOTALL flag for that)
#   e.g. 'f..t' matches a 'f' followed by any 2 chars followed by a 't'
re.findall('f..t', 'which foot or hand fell fastest')

# * is a wildcard that matches zero or more instances of the previous char
#   e.g. 's*t' matches zero or more 's' followed by a 't'
re.findall('s*t', 'which foot or hand fell fastest ssssstupid')

# .* is a common pattern that finds any character zero or more times,
#    but it is GREEDY, meaning it captures as many characters as possible!
#    e.g., everything from the first 'f'to the last 't'
re.findall('f.*t', 'which foot or hand fell fastest')

# .*? with the added ? makes the pattern NOT greedy, so it captures as
#     few characters as possible e.g., everything between 'f' and 't'
re.findall('f.*?t', 'which foot or hand fell fastest')

# + is a wildcard that matches one or more instances of the previous char
#   e.g. 's+t' matches one or more 's' followed by a 't'
re.findall('s+t', 'which foot or hand fell fastest ssssstupid')

# ? is a wildcard that matches zero or one instance of the previous char
#   e.g. 'fo?' matches 'f' followed by zero or one 'o' (thus not greedy)
re.findall('fo?', 'which foot or hand fell fastest')

#   whereas 'fo*' matches 'f' followed by zero or more 'o' (greedily!)
re.findall('fo*', 'which foot or hand fell fastest foooool')
#   and 'fo+' matches 'f' followed by one or more 'o' (greedily!)
re.findall('fo+', 'which foot or hand fell fastest foooool')

re.findall('fo+?', 'which foot or hand fell fastest foooool')
#   of course 'fo' matches 'f' followed by one 'o'
re.findall('fo', 'which foot or hand fell fastest foooool')


# \ escapes string literals e.g., use '\[' to find the bracket char

# \  also defines special sequences:
# \b word boundary
# \d matches any decimal digit, same as [0-9]
# \D matches any non-digit character, same as [^0-9]
# \s matches any whitespace character, same as [ \t\n\r\f\v]
# \S matches any non-whitespace character, same as [^ \t\n\r\f\v]
# \w matches any alphanumeric character, same as [a-zA-Z0-9_]
# \W matches any non-alphanumeric character, same as [^a-zA-Z0-9_]

re.findall('\s[^aeiouy]', 'which foot or hand fell fastest')
re.findall('\w+', 'which foot or hand fell fastest') # words

txt = "He was carefully disguised yet he was quickly found (polyonymy)."
re.findall(r"\w+ly", txt)           # find all 'adverbs' in the text
re.findall(r"\w+ly\b", txt)         # 'ly' at end of word -> word boundary
re.findall("\w+ly\\b", txt)         # using raw string (clearer) or escape

# Caution: backslash is used both by strings and by regex; we need to prevent
# regex metacharacters to be interpreted first as string metacharacters!
# Use r or R (for "raw") before the string. Or use \ as escape char.

re.findall("\w+ly\b", txt)          # now looking for \b the backspace char!
re.findall("\w+ly", txt)            # still works since \w is not "special"

re.findall(r"\bis\b", "The crisis is over.") # searching for word 'is' alone
re.findall("\bis\b", "The crisis is over.") # \b interpreted as backspace: []


# ^ matches the start of a line or string (different from ^ inside brackets)
# $ matches the end of a line or string if multiline search is used
re.findall('^s\S+', 'she sells sea sells on the sea shore')

# { } specify a min/max number of instances: x{m,n} means 'x' at least
#     m times and at most n times (inclusive); thus {,} is the same as *
#     and {1,} is the same as + and {0,1} is the same as ?
re.findall('fo{2,4}', 'which foot or hand fell fastest foooool')
re.findall('fo{2,4}[^o]', 'which foot or hand fell fastest foooool')



################################
##
##  GROUPS AND BACK-REFERENCES
##


# ( ) specify the matching results to be extracted (grouping)
#     i.e., which part(s) of the pattern is returned
htm = '<html><head><title>Tutorial</title><body>etc.'
re.findall('<title>.*</title>', htm)
re.findall('<title>(.*)</title>', htm) # extract title string only

re.findall(r"(\w+)ly\b", txt)       # extract adverb's / verbs' root only

re.findall('\w+(ed|ing)', 'he came, looked, called, then left, wondering')
re.findall('(\w+)(ed|ing)', 'he came, looked, called, then left, wondering')
# ?: specify non-grouping parentheses
re.findall('(\w+)(?:ed|ing)', 'he came, looked, called, then left, wondering')


# \1 \2 ... \n back-references refer to the contents of the matching groups,
# in the same order: \1 is the first group, \2 is the second group, etc.
# e.g. to find matching HTML tags:
re.findall('<(.+)>', htm)           # oops again (greedy match)
re.findall('<(.+?)>', htm)          # non-greedy match!
re.findall('<([^>]+)>', htm)        # same but faster (no backtracking)

htm1 = htm + '<h1>Section</h1><p>bla bla bla</p>'
re.findall('<([^>]+)>.*</[^>]+>', htm1) # find open/close tags (wrong way) 
re.findall('<([^>]+)>.*</\\1>', htm1) # matching tags using a back-reference
re.findall(r'<([^>]+)>.*</\1>', htm1) # same, using raw string (no \ escape)

# Using back-references to replace a matched string
re.sub('<title>(.*)</title>', 'Bibliography', htm) # wrong: replaces tags too
re.sub('(<title>)(.*)(</title>)', r'\1Bibliography\3', htm) # correct


# Example of parsing a URL to get the domain extension (again)
url = 'http://docs.python.org/3/tutorial/interpreter.html'

# this example can be done using string functions and slicing i.e.
url.split('://')[-1].split('/')[0].split('.')[-1]
# now, using a regular expression
re.findall('://.*\.(.*?)/', url)[0]

# step by step:
re.findall('://(.*)', url)          # find '://', keep right part only
re.findall('://(.*/)', url)         # stop at '/', but search is greedy!
re.findall('://(.*?/)', url)        # non-greedy, keep the first match only
re.findall('://(.*?)/', url)        # same except / is not returned
re.findall('://(.*?)\.(.*?)/', url) # grabs one only, leaves too many
re.findall('://(.*)\.(.*?)/', url)  # greedy! grabs all '.' before last
re.findall('://.*\.(.*?)/', url)

re.findall('://(.*?/){3}', url)     # ex. to keep the third match only



################################
##
##  COMPILING REGEX PATTERNS
##

# Python can COMPILE regular expressions, for increased performance!

pat = re.compile('://.*\.(.*?)/')
pat
pat.findall(url)[0]                 # same as above, but faster!

p = re.compile('f[a-z]*')
p.findall('which foot or hand fell fastest')

for m in p.findall('which foot or hand fell fastest'):
    print(m) 

# but, findall() explicitly generates the list: better use an iterator
fit = p.finditer('which foot or hand fell fastest')

for m in fit: print(m.group())      # for each match, print the string

for m in p.finditer('which foot or hand fell fastest'): # new/reset iterator
    print(m.span())                 # for each match, print start/end pos


# See also section 10. Reflection and Meta-programming, for compiling Python
# functions, code fragments, etc.



################################
##
##  MORE FUNCTIONS AND EXAMPLES
##
    

# String split can only use a single delimiter throughout; regex split can
# break a string apart using a regular expression as delimiter!
p = re.compile(r'f...\b')
p.split('which foot or hand fell fastest')

p1 = re.compile(r'\W+')             # one or more non-alphanumeric character
p1.split('which foot or hand fell fastest')
p1.split('which foot, or hand; fell fastest? | with punctuation')


# Substitute the matched regular expression with another string
p.sub('f---', 'which foot or hand fell fastest')
p.subn('f---', 'which foot or hand fell fastest, fool?')
p.sub('f---', 'which foot or hand fell fastest, fool?', count=2)

print(p)                            # compiled regex (object)
print(p.pattern)                    # regex pattern (string)


# Greedy vs. not-greedy matching
htm = '<html><head><title>Tutorial</title><body>etc.'
re.match('<.*>', htm).group()       # matches all from first < to last >
re.match('<.*?>', htm).group()      # matches from first < to first >
re.match('<.*?>', htm).span()


# Matching vs. searching
re.match('<title>(.*)</title>', htm)           # None - no match
re.search('<title>(.*)</title>', htm)
re.search('<title>(.*)</title>', htm).group()  # what is matched
re.search('<title>(.*)</title>', htm).groups() # what is found
re.search('<title>(.*)</title>', htm).span()   # where it is found

re.search('<([^>]+)>(.*)</\\1>', htm).groups() # 1st group for back-reference
re.search(r'<([^>]+)>(.*)</\1>', htm).groups() # 2nd group for extraction

re.search(r'<([^>]+)>(.*)</\1>', htm).group(2) # get second group by index
re.search(r'<([^>]+)>(?P<string>.*)</\1>', htm).group('string') # by name!

re.search('<(head|title)>(.*)</', htm).groups() # first group for OR
re.search('<(?:head|title)>(.*)</', htm).groups() # non-grouping


# note: HTML and XML have a very complex syntax; use the html and xml modules!


# Because regex can become rather complex, it is possible to format them on
# multiple lines, and also to add comments! This is the 'verbose' mode.
# e.g.
name_pattern = "(\w+)\s+(?:([\w.]+)\s+)?(\w+)"  # compact but cryptic
name_pattern = """
    (\w+)               # first name
    \s+                 # space(s) separator
    (?:([\w.]+)\s+)?    # optional middle name or initial, and space(s)
    (\w+)               # last name
    """
re.search(name_pattern, 'John M. Coetzee', re.VERBOSE)

# In verbose mode, whitespace chars (spaces, tabs, linefeeds) are ignored.
# (So to match a space, it needs to be escaped with a backslash.)
# Comments are also ignored (obviously!) They're just like Python comments.
# Lastly, the re.VERBOSE flag must be added as arg for the regex to work.

compiled_name_pattern = re.compile(name_pattern, re.VERBOSE)
re.search(compiled_name_pattern, 'John M. Coetzee').groups()


# See also tutorial slides about Regular Expressions syntax and usage.
# Many online tools are available e.g. @ https://regex101.com/#python
# also many reference sites e.g. @ http://www.regular-expressions.info



################################
##
##  APPLICATIONS OF REGEX
##


# Applications of regular expressions include:
# - Parsing: identifying pieces of text that match certain criteria
# - Searching: locating substrings that can have more than one form, for
#   example, finding any of “pet.png”, “pet.jpg”, “pet.jpeg”, or “pet.svg”
#   while avoiding “carpet.png” and similar
# - Replacing: for example, finding "bicycle" or "human powered vehicle"
#   and replacing either with "bike"
# - Splitting: breaking a string into multiple substrings everywhere a
#   certain delimiter appears (a space, colon, slash...)
# - Validating: checking whether a piece of text meets some criteria, for
#   example, if it contains a currency symbol followed by digits


# The following examples are related to the concept of language grammar,
# where a regex is used instead of the more conventional BNF notation.
# Included are two grammars for roman numerals and US phone numbers.


# Here is an example for validating roman numerals
roman_numeral_pattern = """
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """

re.search(roman_numeral_pattern, 'MCMLXXXIX', re.VERBOSE) # succeeds
re.search(roman_numeral_pattern, 'MCMLXXXXIX', re.VERBOSE) # fails


# This example shows how to parse US phone numbers
phone_pattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

phone_pattern.search('800-555-1212')
phone_pattern.search('work 1-(800) 555.1212 #1234').groups()


# Also: simulating 'scanf' and 'sscanf' in Python (because there aren't any).
# Regular expressions can serve the same purpose, and are more powerful.
# e.g.
# To extract both filename and numbers from the following input string
#     /usr/sbin/sendmail - 0 errors, 4 warnings
# one could use a scanf/sscanf format such as
#     "%s - %d errors, %d warnings"
# The equivalent regular expression would be
#     (\S+) - (\d+) errors, (\d+) warnings

# In simple cases we can use zip and list comprehensions, e.g.:
input_str = '1 3.0 false hello'
[t(s) for t,s in zip((int,float,bool,str), input_str.split())]
#
# but for more complex cases we need regular expressions:
input_str = '1:3.0 false,hello'
[t(s) for t,s in zip((int,float,bool,str),
 re.search('^(\d+):([\d.]+) (\w+),(\w+)$', input_str).groups())]



##
##  END
##
