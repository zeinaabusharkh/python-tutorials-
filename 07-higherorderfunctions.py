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
##  07. Higher-Order Functions and Comprehensions: map, filter, reduce, more
##                              generators, meta-functions, comprehensions
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
###   07. HIGHER-ORDER FUNCTIONS AND COMPREHENSIONS
###



# As seen earlier, Python supports several Functional Programming features,
# including Higher-Order Functions: this means functions are objects like any
# other i.e., first-class entities, and can be stored in variables, modified
# dynamically, passed as function arguments, returned as the value of other
# function calls, etc. (cf. Functions and Lambda Expressions section)

# Why iteration? Why do we need 'for loops'? Recall that iteration as such
# only exists because of computer hardware. Mathematically, repetition is
# induction is recursion. It is also about problem solving: programmers work
# mostly by recognizing categories of problems that come up repeatedly and
# remembering the solution that worked last time; therefore, students should
# learn these program patterns (software design patterns) and fill in the
# blanks for each specific problem...

# Here are the most common patterns for repetition, which high-level (a.k.a.
# higher-order) functions can help model and apply easily.
# * The EVERY Pattern - This is when we want to perform the same query to a
#   collection of objects. Typically we collect the results of transforming
#   each item into something else. Functions: apply/map.
# * The KEEP Pattern - This is when we want to choose some of the items in
#   a collection of objects. We collect the results of this selection and
#   forget about the other items. Functions: filter.
# * The ACCUMULATE Pattern - This is when we want to combine some data by
#   applying some process to a collection of objects. We collect the single
#   result obtained from aggregating partial results (e.g. sum, count, etc.)
#   Functions: reduce.
# * The COMBINE Pattern - This is when we apply two or more of the patterns
#   above to produce a more complex process e.g., map-reduce where we first
#   transform all objects in a collection then aggregate all results.
#   Note that COMPOSITION is when we first create a function that is the
#   combination of several simpler functions, and apply it to the data.
# * SIDE EFFECTS occur when we apply a function that does not transform the
#   objects in a collection, and does not calculate some result out of the
#   data, but instead produces a by-product (e.g. print, save, etc.)
# It is a fact than most complex loops are actually a mixture of the above,
# and could be split into component patterns (example of code refactoring).
# In the end there are very few cases where coding a loop is actually needed.
# (cf. Introduction to Functional Programming slides for more...)



################################
##
##  EVERY PATTERN - APPLY/MAP
##


# Example of 'low-level' list processing
nl = [1,2,3,4,5,6,7,8]
rl = []
for i in range(len(nl)):            # bad (imperative or "C style")
    rl.append(nl[i]**2)
rl = []
for n in nl:                        # better
    rl.append(n**2)                 # or: rl += [n**2]

# Map: from list (or other iterable) to list: map(func,iter) -> list
#      one-to-one mapping: [x1, x2, ... xN] -> [f(x1), f(x2), ... f(xN)]
# Use map to repeatedly apply a transformation and collect the results.
# Example above:
map( lambda n: n**2, nl)            # best - applying a lambda expression!


# note: Python has a simple syntax but, not simple enough yet; e.g.
# Python:  map( lambda n: n**2, range(1,1001) )
# Haskell: map ^2 [1..N] 


list( map( lambda n: n**2, nl))     # map is actually a generator
                                    # (cf. Iterators and Generators section)

list( map( int, ['1','2','3','4'])) # applying a (named) function

map( print, ['1','2','3','4'])      # which result? (side effect!)

list( map( lambda n: n**2, map( int, ['1','2','3','4']))) # composition
list( map( lambda n: int(n)**2, ['1','2','3','4'])) # same, coded manually


cards = ['1S','3C','08D','QH','7C','10H','JD','13S']
list( map( lambda s: s[-1], cards))
sorted( set( map( lambda s: s[-1], cards))) # [FP]
# print card values
list( map( lambda s: int(s[:-1]) if s[:-1].isnumeric() else 0, cards))

list( map( lambda N: 0.70*80+0.30*N, range(40,100,5))) # ex. from Intro


list( map( lambda n: n%2 != 0, [1,2,3,4,5]))

def odd(n): return n%2 != 0
list( map( odd, [1,2,3,4,5]))

any( map( odd, [1,2,3,4,5]))        # true if any is true (logical OR)
all( map( odd, [1,2,3,4,5]))        # true if all are true (logical AND)



################################
##
##  KEEP PATTERN - FILTER
##


# Filter: from list (or other iterable) to sublist: filter(func,iter) -> list
# Use filter to repeatedly apply a predicate and select items accordingly.
# Example above:
list( filter(odd, [1,2,3,4,5]))

list( filter( lambda x: x%2 != 0, nl)) # filter is also a generator

list( filter( lambda s: not s[0].isdigit(), cards))

list(filter( lambda x: x**3 - 15*x**2 + 66*x - 80 == 0, range(1,20)))



################################
##
##  ACCUMULATE PATTERN - REDUCE
##


# functools module for higher-order functions
from functools import reduce        # (used to be in main module)


# Reduce: from list (or other iterable) to value: reduce(func,iter) --> value
# Use reduce to repeatedly apply a function and aggregate the results.
# Example of a sum:
reduce(lambda x,y: x + y, [1,2,3,4,5]) # evaluated as: ((((1+2)+3)+4)+5)

sum([1,2,3,4,5])                    # same, using built-in sum function
sum(x for x in [1,2,3,4,5])

reduce(lambda x,y: x * y, nl)       # product! (no built-in function)

reduce(lambda x,y: x if x < y else y, [10,7,21,5,33,14,50])
min([10,7,21,5,33,14,50])           # same, using built-in min function



################################
##
##  COMBINE PATTERN
##


# Map-Reduce - a common programming idiom, where we apply some transformation
# and aggregate the results into one. (It is also Google's algorithm of fame:
# map search query to multiple servers and aggregate results to client...)

v1 = [1, 2, 3]
v2 = [7, 5, 3]
reduce(lambda x,y: x+y, map(lambda x,y: x*y, v1, v2)) # dot product!

sum([x*y for x,y in zip(v1, v2)])   # same, using comprehension
sum(x*y for x,y in zip(v1, v2))


# Cards example again
import operator                     # for add, sub, mul... (cannot use + * -)
reduce(operator.add, map(lambda x,y: x*y, v1, v2))

reduce(operator.concat, map( lambda s: s[-1]+'-', cards)) # string +

reduce(operator.add,
       map( lambda s: int(s[:-1]) if s[:-1].isnumeric() else 0, cards))
# same as
reduce(operator.add,
       map( lambda s: int(s[:-1]),
            filter(lambda s: s[:-1].isnumeric(), cards)))
# also
sum(map( lambda s: int(s[:-1]),
         filter(lambda s: s[:-1].isnumeric(), cards)))

# note: Functional Programming is all about function COMPOSITION; e.g.
# Python:  sum( map( lambda n: n**3, range(1,1001) ))
# Haskell: (sum . map(^3)) [1..N]

# In Python we apply a function and get a result, to which we apply another
# function, etc. -> cascade of function calls f(g(h(x))) or x.h().g().f()
# In pure FP like Haskell we build the function via composition (f.g.h) then
# apply it -> only one function call, allows optimization... (f.g.h)(x)


# "To calculate the factorial of n, multiply all numbers from 1 to n."
# (i.e. "apply a multiplication function to all numbers from 1 to n.")

def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

factorial(50)

def product(iterable, start=1):
    return reduce(operator.mul, iterable, start)
product(nl)
product(range(1,6))                 # usage similar to sum()

def factorial(n):
    return product(range(1,n+1))    # factorial defined using product

fact = lambda n: product(range(1,n+1)) # equivalent lambda expression

# note: Haskell: fact n = product [1..n]


# Slightly obfuscated example (the aulde rot13 cipher)
def rot13(s):
    return reduce(lambda hold,nixt:
                  hold+chr(((ord(nixt.upper())-65)+13)%26+65), s, '')
text='ZNLORABGGBBHFRSHY'
rot13(text)
rot13(rot13(text))



################################
##
##  MORE HIGH-ORDER FUNCTIONS
##


# functions that implement less common but useful patterns


from itertools import accumulate, starmap, takewhile, zip_longest, compress
# also: chain, compress, filterfalse, groupby, repeat, tee... (all generators)

list( accumulate([1,2,3,4,5]))      # produces 1 3 6 10 15

list( starmap(pow, [(2,5), (3,2), (10,3)])) # 32 9 1000
# same as
list(map( lambda t: pow(t[0],t[1]), [(2,5), (3,2), (10,3)]))

# if data in separate list:
pv,pe = [2,3,10],[5,2,3]
list( map(pow,pv,pe))

sum( starmap(operator.mul, zip(v1,v2))) # dot product again


takewhile(lambda x: x<5, [2,4,6,4,8]) # gets 2 and 4

list( zip_longest('ABCD', 'xy', fillvalue='_')) # yields Ax By C- D-

numvalues = [1,2,3,4,5,6,7]
selectors = [True,False,True,True,False,True,False]
list(compress(numvalues,selectors))


# also: islice, combinations, permutations, combinations with replacement
from itertools import islice, combinations, permutations
list(islice(numvalues,2,6))

list(combinations('ABCD', 2))
list(permutations('ABCD', 2))


# also: Itertools Recipes @ https://docs.python.org/3/library/itertools.html



################################
##
##  META FUNCTIONS
##


# A function that creates a function! (See also log example earlier)
def make_adder(n):
    def adder(x): return x+n
    return adder

f33 = make_adder(33)                # creating a new adder function
f33 (5)                             # calling the function

def make_adder(n):
    return lambda x: x + n          # same, but simpler

f42 = make_adder(42)
f42 (3)
make_adder(100) (3)                 # same, without a reference

(lambda x: x + 20) (3)              # lambda expression = anonymous function

mad = make_adder
mad.__name__                        # name attribute
f33.__name__                        # 'adder' function
f42.__name__                        # just a lambda

# note: this is similar to Curried Functions (see also Continuations) e.g.
# add(x,y) is really make_adder(x) (y) and each function has one argument.


# A meta function for automatically tracing a function!
def fib(n):
    if n is 0 or n is 1: return 1
    else: return fib(n-1) + fib(n-2)

def trace(f):
    def traced_f(x):
        print(f.__name__,'(',x,')', sep='')
        value = f(x)
        print('return', repr(value))
        return value
    return traced_f

fib(3)
fib = trace(fib)                    # replaces fib with the traced version!
fib(3)

# Note: the above 'trace' function assumes f requires a single argument. To
# generalize, we need 'traced_f' to accept a variable number of arguments.
# Also, indenting the output would be make it much clearer.

# Using the (built-in) decorator pattern allows defining a function and
# enable 'trace' on it in a single block of code! (but. no indent :(
# Note that in Python decorators are functions (not in Java...)
@trace
def fib(n):
    if n is 0 or n is 1: return 1
    else: return fib(n-1) + fib(n-2)



################################
##
##  COMPREHENSIONS
##


# List comprehension: [f(x) for x in items] same as map(f,items) 

# Implicit lambda expression, with intuitive syntax
[x**2 for x in range(1,11)]

for n in [x**2 for x in range(1,11)]: print(n)

for n in map(lambda x: x**2, range(1,11)): print(n) # same using map


# List comprehension with conditional statement - map and filter mixed
[x for x in range(20) if x%3 != 0]

# Bissextile year example
leapyears = [y for y in range(1900,1940)
             if (y%4 == 0 and y%100 != 0) or (y%400 == 0)]

leapyears = [y for y in range(1900,1940,4) if y%100 != 0 or y%400 == 0]
print(leapyears)

# File extension filter example
files = {"a.txt", "b.jpg", "C.HTM", "d.doc", "E.pdf", "f.html",}
htmlf = {f for f in files if f.lower().endswith((".htm", ".html"))}
print(htmlf)                        # yields {'C.HTM', 'f.html'}


# Building complex sequences
[(x, x**2) for x in range(1,7)]     # list (sequence) of tuples
{x : x**2 for x in range(1,7)}      # dictionary (not nec. ordered)
{x**2 for x in range(1,7)}          # set (not nec. ordered)

(x**2 for x in range(1,7))          # tuple? no it's a generator!
tuple((x**2 for x in range(1,7)))   # now a tuple is created (constructor)
sum(x**2 for x in range(1,7))       # implicit generator used

# Multi-dimensional list comprehension
[(x, y) for x in [1,2,3] for y in [3,4]]
[(x, y) for x in [1,2,3] for y in [3,4] if x != y]


from math import pi
[round(pi, p) for p in range(1, 8)]

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12] ]
[ [row[i] for row in matrix] for i in range(4)] # matrix transpose!

list(zip(*matrix))                  # same, using built-in functions!

for a,b,c in zip(*matrix): print(a,b,c) # equivalent loop, shows as matrix


# Quick sort, functional programming style!
def qsort(L):
    return ( qsort( [a for a in L[1:] if a < L[0]])
             + [L[0]] +
             qsort( [b for b in L[1:] if b >= L[0]]) ) if len(L)>1 else L

qsort([1,5,7,4,2,6,9,0,3,8])

            
# Classic FizzBuzz programming exercise again
for k in range(1, 101):
    words = [word for n, word in ((3, 'Fizz'), (5, 'Buzz')) if not k % n]
    print(''.join(words) or k)


# note: For really complex cases, it is advised to use 'for' loops rather
# than comprehensions (esp. with nested loops, multiple conditionals...)
# The following example are good but not very readable (indent would help).


# Print the first 20 Fibonacci numbers
print(list(map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1:
f(x,f), range(20))))

# Print all prime numbers less than 1000
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))


# Print an ASCII version of the Mandelbrot fractal set
"""
print((lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+y,map(lambda y,
Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
>=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24))
#    \___ ___/  \___ ___/  |   |   |__ lines on screen
#        V          V      |   |______ columns on screen
#        |          |      |__________ maximum "iterations"
#        |          |_________________ range on y axis
#        |____________________________ range on x axis
"""


##
##  END
##
