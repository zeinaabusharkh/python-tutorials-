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
##  03. Flow Control and Repetition: comparison, conditionals, iteration;
##                                   range, enumerate, zip; and more ...
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
###   03. FLOW CONTROL AND REPETITION
###



################################
##
##  COMPARISON
##


x = y = 5
0 < x
0 < x or 0 < y                      # intuitive syntax! (and, or, not)
x > 1 and x <= 10                   # "C style" comparison
1 < x <= 10                         # same, Python style (a.k.a. 'pythonic')

0 < x == y                          # same as 0 < x and x == y
x is y                              # intuitive again (but see below)

5 and True                          # returns True
5 and 10                            # returns 10
10 or False                         # 10 (allows cascading operations)

# Order of precedence: or, and, not, in, not in, is, is not, <, >, ...
# e.g.
not False and False                 # False
not (False and False)               # True
not False or True                   # True
not (False or True)                 # False
False and True or True              # True
False and (True or True)            # False


# Use '==' to compare values, use 'is' to compare objects / references

n1 = 1.23 ; n2 =1.23                # sequential assignment (or 2 lines)
n1 == 1.23                          # same value
n1 is 1.23                          # different identity (object)
n3 = n1
n1 is n3                            # references to the same object

l1 = [1,2,3] ; l2 = [1,2,3]         # 2 identical lists
l1 == l2                            # same value
l1 is l2                            # different identity (object)

# Particular cases:
s1 = 'hi' ; s2 = 'hi'
s1 == s2                            # same value
s1 is s2                            # True! (only one string, like Java)

s3 = ''.join(['h', 'i'])            # creates another string 'hi' 
s1 == s3                            # same value
s1 is s3                            # different identity (object)

2**2 is 4                           # True - Python caches small int
10**3 == 1000                       # True, as expected: same value
10**3 is 1000                       # False, as expected: diff objects



################################
##
##  CONDITIONAL STATEMENTS
##


# If/else
x,y = 4,3
if x > y:
    print("it's true then")         # indentation serves as block delimiter

if x < 0:
    print('negative')
elif x > 0:                         # optional conditions (as many...)
    print('positive')
else:                               # optional default case
    print('zero!')


if (x>=10 and x<100):               # "C style" coding (bad)
    print('2-digit number')

if 10 <= x < 100:                   # "Pythonic" style (good)
    print('2-digit number')

if x > 0:                           # if block
    if y > 0:                       # indented hence nested if block
        z = x * y
    elif y < 0:                     # matching based on indentation
        z = x * -y
    else:
        z = 1
    print('z =', z)                 # back to outer if block
else:
    z = -x * x
print('done')                       # back to main script (top level)


# Equivalent to C/C++ statement: ( Test ? Exec_if_True : Exec_if_False )
# which becomes: Exec_if_True if Test else Exec_if_False [FP]
x, y = 10, 5
minxy = x if x < y else y           # (x) < (y) ? (x) : (y)) in C/C++

# The same syntax is used in lambda expressions (cf. Functions section)
# and comprehensions (cf. Higher-Order Functions section).

# Also to make code shorter - functional style vs. imperative style
def fmax(a, b): return a if a > b else b
# vs.
def imax(a, b):
	if a > b: return a
	else: return b



################################
##
##  LOOP STATEMENTS
##


# While loop
x = 5
while x > 0:
    print("x is", x)
    x = x - 1

# Example calculating and printing Fibonacci numbers
a,b = 0,1
while b < 100:
    print(b)
    a, b = b, a+b


# Forever loop, needs keyboard interrupt (Ctrl+C) to halt:
#while True: pass 

def function_to_code_later(): pass  # used as "to do" marker


# For loop, iterates over anything that is iterable (e.g., a sequence)
for item in [1,2,3]:
    print(item)                     # list
    
lst = [1, 'two', [3, "three", 0x111], "four"]
for item in lst:
    print(item)                     # list all items (Java/Python style)

for i in range(len(lst)):           # same ("C style" - bad)
    print(lst[i])

for i in range(len(lst)):
    print("lst[", i, "] =", lst[i]) # index + item ("C style" again)

for i, v in enumerate(lst):         # same (the Python way!)
    print("lst[", i, "] =", v)


for item in 'a', 'b', 'c':          # tuple
    print(item)

s = "sample string"
for c in s: print(c)                # string as char sequence, as: list(s)

d = { 'fr': "France", 'uk': "United Kingdom", 'it':"italy" }
for k in d.keys(): print(k)         # dictionary keys

for k in d: print(k)                # same (simpler/better)

for v in d.values(): print(v)       # dictionary values

for k in d: print(d[k])             # same

for i in range(20):                 # range iterator: generates all items,
    print(i)                        # one at a time (one per iteration)


# Classic FizzBuzz programming exercise
fizz,buzz = "Fizz","Buzz"
for k in range(1,33):
    if k % 15 == 0:
        print(fizz+buzz)
    elif k % 3 == 0:
        print(fizz)
    elif k % 5 == 0:
        print(buzz)
    else:
        print(k)
    k += 1

# A shorter/better [FP] and more pythonic solution is:
for k in range(1, 101):  # k from 1 to 100
    print('Fizz' * (not(k%3)) + 'Buzz' * (not(k%5)) or k)
    


################################
##
##  MORE ITERATION EXAMPLES
##


# Range iterator / iterable
print(range(5))                     # not a list, actually
type( range(5))                     # it's a range object - an iterator!
list( range(5))                     # converting to list forces iteration

for i in range(5): print(i)         # for loop also forces iteration

set(range(2,8))                     # converting to a set
tuple(range(2,8,2))                 # converting to a tuple, with step of 2
list(range(100,0,-10))              # descending order

# Note: suppose range parameters are given in a list (e.g. passed to a function)
r = [2,12,2]
#list( range(r)) -> TypeError: 'list' object cannot be interpreted as integer
list( range(r[0],r[1],r[2]))        # correct but inconvenient
list( range(*r))                    # need to flatten the list! (also tuple...)

print(enumerate(('a','b','c')))     # enumerate object - another iterator
print(list(enumerate(('a','b','c'))))# converting to list forces iteration


# More loops
rg = range(1, 11, 2)
for ri in reversed(rg):             # iterating in reverse, useful if the
    print(ri)                       # range is not known beforehand (arg)
#for i in range(9,0,-2): print(i)   # same (hardcoded)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):   # converting to a set removes duplicates!
    print(fruit)

d = { "fr":"France", "uk":"United Kingdom", "it":"Italy" }
for k, v in d.items():
    print(k,"<->",v)


# Synchronized iteration!
fstnames = ["Alex", "Bob", "Clara"] 
surnames = ["McGuire", "Nielsen", "Olsen", "Xtra_ignored"]

for n, s in zip(fstnames, surnames):
    print("{}'s surname is {}.".format(n, s))


z = zip(fstnames, surnames)         # zip object - another iterator
print(z)                            # (cf. Iterator / Generator section)
next(z)                             # generates the next item


# Loop else! where code executes after loop completion (like 'finally')
for i in range(5):
    print('i =', i)
else: print('done')                 # here 'else' makes no difference

# Example of identifying prime numbers
for n in range(2, 20):
    for x in range(2, int(n**0.5)): # try all divisors in 2..sqrt(n)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number') # only when not breaking from the loop



##
##  END
##
