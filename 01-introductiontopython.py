###############################################################################
###
###   PYTHON 3: FROM IMPERATIVE TO OBJECT-ORIENTED TO FUNCTIONAL PROGRAMMING
###
###   Copyright Michel Pasquier, 2013-2018
###
###   This comprehensive tutorial is meant to be used interactively in class.
###   By design, it lacks the detailed explanations which are offered by the
###   instructor. For these, and much more, see the many references provided
###   throughout these files as well as on the course site.
###



################################
##
##  TABLE OF CONTENT
##
##  01. Introduction to Python: shell, variables, print, types; for, range,
##                              if/else; numbers; string, slicing, format...
##  02. Sequences and Collections
##  03. Flow Control and Repetition
##  04. Functions and Lambda Expressions
##  05. Classes and Inheritance
##  06. Exceptions and File I/O
##  07. Higher-Order Functions and Comprehensions
##  08. Iterators/Generators and Lazy Data Types
##  09. Regular Expressions and Pattern Matching
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##



###############################################################################
###
###   01. INTRODUCTION TO PYTHON
###


# Python 3 vs. 2: syntax/implementation differences e.g., print(), range().
# Also fixes and improvements e.g., integer division, increment, iterators.
# Many additions e.g., Unicode (UTF-8), lazy structures, and a lot more...
# Use Python 2 for legacy code/libraries only, if needed. Actually, don't.



################################
##
##  INTERACTIVE SHELL
##


# All kinds of calculations e.g
# Instructions / code are executed immediately (no compilation!)
print("Welcome to Python!")

x = 10                              # variable created (virtual machine!) 
x = x * x                           # then updated
print(x)                            # and printed

# or just "inspect" the variable (interpreter only) 
x
#y                                  # error: variable not defined


# Using the shell as a calculator, interactively!
25*7 - 13*4

# Last expression/result available via _ character (interpreter only)
# _ * 2


# The following is also a Python script / program!
price = 1200
vat = 0.15                          # note: no type! (but see later)
price += price * vat
print(price)

# Python script / program = Python code in a text file e.g., test.py
# To run a script, either (1) open in IDLE and run it (via F5 'Run Module'),
# (2) run it directly in a terminal: python test.py, (3) select test.py and
# 'open with' python.exe (In the last two cases a shell window will open and
# then close quickly, unless user input is required or some GUI is started.)
# One can also open a script and execute its content programmatically e.g.:
#exec(open('01-xTkConverterGUIdemo.py').read())


# All kinds of calculations e.g., to estimate someone's final grade:
sofar = 80
final = 72
0.70 * sofar + 0.30 * final

# Or, try many scenarios, programmatically... Example with a 'for' loop
# (cf. Flow Control section) and range Generator (cf. Iterator section).
for final in range(40,100,5):
    print(final, '->', 0.70 * sofar + 0.30 * final)


# All the way to powerful computing e.g., series: 1 + 1/2 + 1/3 + ... + 1/10
# using Higher-Order Functions and Comprehensions (cf. later sections) [FP]
sum(1/x for x in range(1,11))

sum(x**3 for x in range(1,11) if x%2 == 0)


# Experimenting ... typing and evaluating at once e.g., factorial function
# (cf. Flow Control and Functions sections for full details and examples)
def factorial(n):
    if n == 1:                      # if/else block - indent for syntax!
        return 1
    else:
        return n * factorial(n-1)

#factorial(993)                     # a very large number (still fast)
#factorial(1000)                    # RuntimeError: max recursion depth
                                    # exceeded (cf. Exceptions section)

from math import factorial          # import function from math module
from math import factorial as fact

from math import cos as sin ; sin(0) # warning: no check! be careful



################################
##
##  OBJECTS AND TYPES
##


# Dynamic typing! Variables defined as and when declared and initialized.
# Type inference! Variable type is automatically determined by Python (it is
# neither strictly typed, like C++/Java, nor typeless, like Lisp/Scheme...)
x = 5
type(x)                             # 'x' is an object of integer class
x = 'hi!'
type(x)                             # now 'x' is a string object
x = True
type(x)                             # and now it's a Boolean


# Warning: Everything is a 'variable'! even functions, classes, modules...
# Be careful not to override names e.g., str = "hello" or type = 4


# References! (similar to Java)
a = 1
type(a)                             # reference to 'int' object (value 1)
b = a                               # another reference to the same object
a = a + 1
a                                   # now refers to another 'int' object (2)
b                                   # refers to the same old 'int' object (1)

# So, actually: Everything in Python is an object! incl. functions, classes,
# modules, etc. (and almost everything has attributes and methods). Therefore
# every name / variable is merely a reference to an object! Note also that
# many are immutable e.g., bool, int, float, str ... list, and many more!

# One can 'undefine' a variable but it only deletes the name/reference; it
# does not free the memory. For that, Python has garbage collection!
del x
#print(x)                           # NameError: name 'x' is not defined


# Interactive help, about functions, classes, etc.
help
help(print)

# List all instance attributes, functions/methods, and attributes of a class
dir(int)
dir(a)
dir()



################################
###
###   NUMBER TYPES
###


# Definition / assignment
n = 11                              # variable 'n' is defined, of type 'int'
n = "Hello"                         # redefined as a string, of type 'str'

m = n = 10.0                        # sequential assignment (float)
m,n = 17,19                         # parallel assignment!
m,n,p,q = a,b,c,d = [1, 2, 3, 4]    # unpacking: parallel extraction
print(p, d)
m,n = n,m                           # parallel swap! (elegant and fast)


# More numbers and functions
abs(-11)                            # absolute value
print( 12**2 )                      # exponent

5*2**3                              # careful about precedence
15129 ** 0.5                        # square root (et al)
from math import sqrt               # sqrt function only in math module
sqrt(15129)                         # (cf. Modules and Libraries section)

factorial(100)                      # arbitrary precision, hence only two num
2**10000                            # types are needed: 'int' and 'float'

3.1415e-10 / 100                    # floating point number

print(0xFF)                         # hexadecimal literal (base 16)
print(0o10)                         # octal literal
print(0b101010)                     # binary literal

print( hex(19) )                    # string representation (also bin/oct)


# Usual operators... plus integer division
n, d = 7, 3
print(n/d)                          # no type 'declared' so 2.333 is expected

5 / 2                               # correct, intuitive result! (float)
5 // 2                              # floor division (int)

round(9/5)                          # rounding up or down (int)
from math import floor              # ceil and floor in the math module
floor(9/5)                          # same as 9//5


# Complex numbers (immutable)
z = 1+2j                            # notation for 1+2i (more readable)
print(z)
type(z)                             # 'complex' object

z.real                              # real and imaginary parts (attributes)
z.imag                              # accessed directly - eq. to 'getter'

# No 'setter' needed when the object is immutable
#z.real = 4                         # AttributeError: readonly attribute

z * (3j)                            # complex number arithmetic!
1/z
z**-1
abs(z)


# Underscores can be used as visual separators for digit grouping purposes in
# int,float, and complex number literals [v3.6]. This feature was created long
# ago in ADA; now it's in Java 8!
amount = 10_000_000.0
print(amount)			    # written as regular float (no underscore)

flags = 0b_0011_1111_0100_1110
phone = +971_50_123_4567



################################
##
##  STRING TYPE AND SLICING
##


# String definition, using single or double quotes (also triple quotes, later)
'hi!'
s = "abcdefghij"
print(s)
type(s)                             # 'string' object

"hello," + " world"                 # concatenation (new string object)
"hello," " world"

# Parentheses are needed to group multiple lines -- or else use \
txt = ('If a string is too long, break it into a sequence of smaller strings,'
       'each placed on a single line as shown in this example. The sequence'
       'of strings must be surrounded by a pair of grouping parentheses,'
       'so that they will be automatically concatenated back into one.')


"hello, " * 3                       # repetition!
'=' * 40

n = 4                               # allows handing options easily e.g.
print(n, "piece" + (n>1)*'s')       # '4 pieces' vs. '1 piece' (FP style!)
True * 4                            # because True is 1 and False is 0

# String indexing
"hi!" [0]                           # (spaces are optional)
s[1]
s[-1]                               # last item! same as: s[len(s)-1]
s[3]
#s[3] = 'x'                         # strings are immutable (like in Java)

# No character type in Python! 'X' is a string of length 1


# String slicing
s[2:6]                              # substring from index 2 till before 6
s[4:]                               # substring from index 4 till end
s[:4]                               # substring from start till index 3
'J' + 'Python'[1:]
s[:]                                # substring from start to end: a copy!

sh = "Hello"
sh = sh[0:3] + 'p!'                 #  =>  0   1   2   3   4   5
                                    #      +---+---+---+---+---+
sh[-3:]                             #      | H | e | l | p | ! |
sh[-3:-1]                           #      +---+---+---+---+---+
                                    #     -5  -4  -3  -2  -1      <=
s[1:7]
s[1:7:2]                            # scanning by interval of 2
s[5:2:-1]                           # scanning backward

#s[100]                             # -> IndexError exception
s[4:100]                            # smart bounds: no out-of-bound exception!

for k in range(len(s)+1):           # s[:k] + s[k:] is invariant
    print(s[:k] + ' ' + s[k:])      # (same as 's' itself, for any k)

# for c in s: print(c)              # Python-style iteration (no index!) 


# Comparison and search
"hello" < "jello"
"hello" >= 'hi'
'Python' > 'Java' > 'C++' > 'C'     # -> True (alphabetically, but also... ;)

if 'Hel' in sh:                     # check for substring
    print("yes")

'hello'.find('l')                   # index of first occurence
'hello'.rfind('l')                  # index of last occurence

st = 'two for tea and tea for two'
st.count('tea')                     # number of occurences

st.replace('tea', 'coffee')         # substitution (creates a new string)
st.replace(' ','/')

# Search using wildcards and Regular Expressions! (cf. later section)


# More string operations (methods)
len(st)                             # string length - function or method
st.__len__()                        # (cf. Classes and OOP section) [FP]

st.isalpha()                        # checking
"1234".isnumeric()
"john doe".istitle()
"abc".upper()                       # converting
"john doe".title()

"/".join(["dir","subdir","file"])   # joining strings, with separator
'dir/subdir/file'.split('/')        # splitting, based on separator

# note: String objects are immutable hence concatenating many strings together
# is very inefficient (as each concatenation creates a new object). The best
# approach is to place all strings into a list and call join() at the end.

"john henry doe".split()            # N-split (default: space separator)
"john henry doe".split('h')

"john henry doe".partition(' ')     # 2-way split, forward or backward
"john henry doe".rpartition(' ')

# Simple code, thanks to string split, unpacking, and parallel assignment
username, domain = 'monty@python.org'.split('@')

# Example of parsing an(y) URL to get the domain extension! (com,edu,org...)
url = 'http://docs.python.org/3/tutorial/interpreter.html'
url.split('://')[-1].split('/')[0].split('.')[-1] # OO-style cascading [FP]


# note: The str class is quite powerful as is. There is also a string module,
# which offers even more functionality. Then, there are regular expressions
# (re module - cf. later section)...



################################
##
##  QUOTES AND COMMENTS
##


'Python is the "most powerful language you can still read". -- Paul Dubois'


# Quotes
'it does not'
'it doesn\'t'
"it doesn't"                        # having ' and " allows mixing easily
print('\n "Welcome!" I said \n')

# Raw strings, where everything is taken literally
print(" one \n two")
print(r" one \n two")               # clearer than print(" one \\n two")


# Triple quotes for formatting 'as is'
print("""\
Sessions:
   a) Basic
   b) Advanced
   c) Optional
   """)

"""options:
   a) pizza
   b) pasta
   c) other"""

print("""

    Everything should be made as simple as possible, but not simpler.
        -- Albert Einstein

""")

# Triple quotes for (multi-line) block commenting
"""
    _____________________________________________________________________
   |                                                                     |
   |                  /^\/^\                                             |
   |                _|__|  O|                                            |
   |       \/     /~     \_/ \                                           |
   |        \____|__________/  \                                         |
   |               \_______      \                                       |
   |                       `\     \                 \                    |
   |                         |     |                  \                  |
   |                        /      /                    \                |
   |                       /     /                       \\              |
   |                     /      /                         \ \            |
   |                    /     /                            \  \          |
   |                  /     /             _----_            \   \        |
   |                 /     /           _-~      ~-_         |   |        |
   |                (      (        _-~    _--_    ~-_     _/   |        |
   |                 \      ~-____-~    _-~    ~-_    ~-_-~    /         |
   |                   ~-_           _-~          ~-_       _-~          |
   |                      ~--______-~                ~-___-~             |
   |                                                                     |
   |_____________________________________________________________________|

"""



################################
##
##  STRING FORMAT AND %
##


# String format, using {} as placeholder
"1 plus 2 equals {}".format(3)
'1: {}, 2: {}, 3: {}'.format('A', 0xFFFF, 3+2j) # default order
'3: {2}, 2: {1}, 1: {0}'.format('a', 'b', 'c')  # custom order

# Using positional arguments as references
'complex {0} has a real part {0.real}\
 and imaginary part {0.imag}'.format(3+2j)
'1: {0[0]}, 2: {0[1]}, 3: {0[2]}'.format(['a', 'b', 'c'])
'2-1: {0[1][0]}, 2-2: {0[1][1]}'.format(['a', ['b','c'],'d'])

# Using keyword arguments instead (more flexible)
'Coords: {lat}, {lon}'.format(lon='-115.8W', lat='37.2N')


# Like Java, Python supports Unicode! (UTF-8 by default, not UTF-16)
print('Hello, \u0057\u006F\u0072\u006C\u0064!')
print(r'Hello, \u0057\u006F\u0072\u006C\u0064!')    # string 'as is'


# Left/right/center justification
'{:<30}'.format('left aligned')
'{:>30}'.format('right aligned')
'{:_^30}'.format('centered')        # replacing filler (default is space)

# Table-like formatting
for n in range(1, 13):
    print('{:3d} {:4d} {:5d}'.format(n, n*n, n*n*n))

# Printing again, changing the default separator (no space)
print("There are <", 2**32, "> possibilities!", sep='')  # also end=''


# Old 'printf'/'scanf' style (only int, str, and double are supported):

from math import pi                 # pi in math module (48 decimals)
print(pi)                           # default prints 15 decimals

print('The value of PI is approximately %.4f' % pi)   # 4 decimals

for n in range(1,11):
    print(('%'+str(n+6)+'.'+str(n)+'f') % pi) # varying number of decimals

# Be careful (again), this is Python:
pi = 'apple'                        # destroys original pi value!
from math import pi                 # (only way to restore it)



################################
##
##  STRING LITERALS [v3.6]
##

import datetime
name, age, bday, value = 'Fred', 50, datetime.date(1991, 10, 12), 421

f"My name is {name}. I am {age+1}. I'm born on is {bday:%A, %B %d, %Y}."


# More concise and readable than string format; for example, the directive
'The value is {}.'.format(value)
# can be written more concisely using an f-string:
f'The value is {value}.'

# Provides additional formats not available with %-formatting or string format
f'input={value:#06x}'
f'{bday} was on a {bday:%A}'


# Type conversion may be specified (similar to string format): '!s' calls str()
# on the expression, '!r' calls repr(), and '!a' calls ascii(). Compare e.g.:
f'He said his name is {name}.'
f'He said his name is {name!r}.'

# Backslashes may not appear inside a f-string; so the correct way to have a
# literal brace appear in the resulting string value is to double the brace:
f'{{ {4*10} }}'

# Yes, f-strings are evaluated! Another example:
f'result={factorial(5)}'
# which is equivalent to
'result={}'.format(factorial(5))
'result=' + str(factorial(5))

for n in range(2,11):
    print(f'{pi:{n+6}.{n}}') 	    # varying number of decimals (more concise)



################################
##
##  PYTHON CODING STYLE
##


# Use 4-space indentation, and no tabs.
# Wrap lines so that they don't exceed 79 characters.
# Use blank lines to separate functions, classes, and large blocks of code.
# When possible, put comments on a line of their own.
# Use doc strings.
# Use spaces around operators and after commas, but not directly inside
#     bracketing constructs: a = f(1, 2) + g(3, 4); not f( 1, 2 )...
# Name your classes and functions consistently; the convention is to use
#     CamelCase for classes and lower_case_with_underscores for functions
#     and methods. Use self as the name for the first method argument.
# Don't use fancy encodings if your code is meant to be used in
#     international environments. Python's default UTF-8 works best.
#
# Style Guide for Python Code @ http://legacy.python.org/dev/peps/pep-0008/



################################
##
##  THE ZEN OF PYTHON
##


print("""

Python's most famous programming "Easter egg":

>>> import this

""")
import this                         # (cf. Misc section for more Easter eggs)



##
##  END
##
