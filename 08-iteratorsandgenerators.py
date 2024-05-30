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
##  08. Iterators/Generators and Lazy Data Types: containers etc., iterables,
##                    iterators, generator functions, generator expressions
##  09. Regular Expressions and Pattern Matching
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##



###############################################################################
###
###   08. ITERATORS / GENERATORS AND LAZY DATA STRUCTURES
###



################################
##
##  CONTAINERS / SEQUENCES
##


# A container / sequence is a finite data type that stores items, lives in
# memory, and typically holds all its data in memory too. It must support the
# membership operator in() and the size function len(). Most containers are
# iterables (so they work in a 'for' loop, to get every item) but not all.
#
# Examples in Python include: list (and deque), set (and frozenset), dict
# (and defaultdict, OrderedDict, Counter), tuple (and namedtuple), str...

1 in [1,2,3]                        # list membership
4 not in {1,2,3}                    # set membership
3 in {1:'foo',2:'bar',3:'nil'}      # dict membership (checks the key)
'b' in 'foobar'                     # string membership

len([1,2,3]) == len({1:'foo',2:'bar',3:'nil'}) == len('foo') # size


# A container implements the in() function as __contains__() and the len()
# function as __len__().


# Containers / sequences can be created either explicitly, or by calling a
# constructor (conversion), or programmatically, or using comprehensions.

le = [1,2,3,4,5,6]                  # explicit
lc = list('foobar')                 # constructor
lr = list(range(1,6))

lp = []
for n in [1,2,3,4]: lp.append(1/n)  # implicit/programmatically with for
[1/n for n in [1,2,3,4]]            # or using comprehension syntax
#not map(lambda n: 1/n, [1,2,3,4])  # but a generator is different



################################
##
##  ITERABLES
##


# An iterable is a class that allows iterating over its instances' content.
# It must either be an iterator or return an iterator, so that all its items
# can be retrieved one by one (e.g., by a 'for' loop).
#
# Iterables include data structures, such as containers/sequences (list, set,
# tuple, dict...) as well as open files, open sockets, URLs, etc. Iterables
# may be finite or may just as well represent an infinite source of data.

for n in [1,2,3]: print(n)          # list iterable
for k in {1:'foo',2:'bar',3:'nil'}: print(k) # dict iterable
for c in 'foobar': print(c)         # string iterable

for ln in open('4python-dev.txt'):  # file iterable
    if ln[0] == '*' and ln[-2] == 'S':
        print(ln)


# One can manually create an iterator and use it. The example below creates
# a list iterator and repeatedly retrieves the next list item.

lst = [1,2,3]                       # iterable list
liter = iter(lst)                   # iterator on the list
print(liter)
next(liter)                         # getting the next list item
next(liter)                         # until items are exhausted

# The 'for' loop automatically creates an iterator on the given iterable and
# repeatedly calls the next() function to get every item, until there is no
# more - then it catches the StopIteration exception raised by next().
for n in [1,2,3]: print(n)

# Disassembling this code shows the explicit call to GET_ITER, which is like
# invoking iter(). The FOR_ITER instruction is equivalent to calling next()
# repeatedly to get every item (not shown in the byte code because it is
# optimized for speed in the interpreter).
import dis
dis.dis('for n in [1,2,3]: print(n)')


# An iterable implements the __iter__() function to return an iterator, which
# is either itself, or one created by iter(), or a custom iterator.

# Example making a deck of cards iterable
class Card(object):
    FACE = {11: 'J', 12: 'Q', 13: 'K'}
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank if rank <=10 else Card.FACE[rank]
    def __str__(self):
        return "%s%s" % (self.rank, self.suit) # 1S or 4D or QH ...

class Deck(object):
    SUITS = ['S', 'D', 'C', 'H']
    def __init__(self):             # list of 52 cards (cf. Comprehensions)
        self.cards = [Card(r, s) for s in Deck.SUITS for r in range(1, 14)]

    def __iter__(self):
        return iter(self.cards)

# Since a list is iterable, we can always iterate over the list of cards:
deck = Deck()
for card in deck.cards: print(card, end=' ')

# But now that Deck implements __iter__(), it is an iterable and we can use
# the shorter and more intuitive: "for every card in the deck ..."!
for card in deck: print(card, end=' ')



################################
##
##  ITERATORS
##


# An iterator a stateful object that allows iterating over a given container/
# sequence, etc. It must implement the next() function, that will produce the
# next item when called. Iterators are always iterables, by definition.
#
# Python include many examples of iterators, some are built-in (range, zip,
# enumerate... but also map, filter) and some are in the itertools module.
from itertools import count, cycle, islice

# An iterator may produce an infinite sequence automatically:
counter = count(start=10)
print(counter)
next(counter)
next(counter)
# ...
#while True: print(next(counter))   # infinite loop
print(counter)

# An iterator may produce an infinite sequence from a finite one:
colors = cycle(['Red', 'Green', 'Blue'])
for n in range(9): print( next(colors), end=' ')

# Iterators and generators realize lazy data structures / datatypes! [FP]
# Unlike containers / sequences that hold all their data in memory and must
# therefore be finite, lazy data structures can be infinite. Their items are
# only created one at a time, as and when requested.

# An iterator may also produce a finite sequence from an infinite one:
sevenColors = islice(colors, 0, 7)
for color in sevenColors: print( color, end=' ')


# An iterator implements the next() function as __next__(). Any object that
# has a __next__() function is therefore an iterator. As mentioned, any object
# that returns an iterator via the __iter__() function is iterable.


# Example making a Fibonacci numbers iterator! Note that it is an iterable,
# because of the __iter__() function, and it is its own iterator, because of
# the __next__() function. (No point creating a separate class...)
class Fib:
    def __init__(self):
        self.prev,self.curr = 0,1   # set initial state / values
    def __iter__(self):
        return self
    def __next__(self):             # next() function:
        fibval = self.curr
        self.curr += self.prev      # calculate next value
        self.prev = fibval          # update state
        return fibval               # return current value

#for n in Fib(): print(n, end=' ')  # infinite!

fibiter = Fib()                     # instance of Fib iterator
for n in range(10): print( next(fibiter), end=' ') # for loop calls next()

list( islice(fibiter, 0, 10))       # isslice iterator calls next()

# The state of the iterator (Fib object) is fully kept inside prev and curr
# instance variables. Every call to next() does two things: modify its state
# (for the following next() call) and return the result of the current call.



################################
##
##  GENERATORS (FUNCTIONS)
##


# A generator function is a special kind of iterator: it is a simple function
# that automatically creates and returns an iterator, without having to code
# the class and __iter__() and __next__() functions. A generator function
# is characterized by the presence of the 'yield' operator.
#
# We call the generator only once, to get the iterator (it's like a 'factory'),
# then we can repeatedly call the next() function on the iterator as before.
# In Python, many built-in iterators are actually implemented as generators.

# Example of a Fibonacci numbers generator:
def fib():
    prev, curr = 0, 1
    while True:                     # allows a potentially infinite sequence
        yield curr                  # pause the loop and returns the value
        prev, curr = curr, prev + curr # update state / values

#for n in fib(): print(n, end=' ')  # infinite! (same syntax as above!)

fibgen = fib()                      # iterator created by fib()
for n in range(10):                 # for loop calls next()
    print( next(fibgen), end=' ')

list( islice(fibgen, 0, 10))        # isslice iterator calls next()

# The state of the generator (returned by fib()) is kept inside prev and curr
# function variables. Every call to next() runs one iteration of the loop,
# which does two things: modify its state and return the current value.


# Example: Lazy data type for generating an infinite sequence of integers
def integers():
    """set of natural numbers"""
    n = 0
    while True:
        yield n
        n += 1

intiter = integers()
next(intiter)
next(intiter)
# ...
list( islice(intiter, 100, 120))

#for n in integers(): print(n)      # infinite again


# Generators can be built from other generator/s; examples:
map(lambda n: n**2, range(1,1000000))

def squares():
    for n in integers():
        yield n * n

list( islice(squares(), 10, 20))

def take(n, seq):
    """returns first n values from a given sequence / iterable"""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration: pass
    return result

print( take(10, squares()))



################################
##
##  GENERATOR EXPRESSIONS
##


# Generator expressions are... comprehensions! (which are equivalent to map or
# filter...) See Higher-Order Functions and Comprehensions for many examples.

# In the cases below, all items must be produced (exhaustively) because list,
# set, and dictionary must be created, which are explicit data structures.
numbers = [1,2,3,4,5,6,7,8]
[n**2 for n in numbers]             # list comprehension
{n**2 for n in numbers}             # set comprehension
{n : n**2 for n in numbers}         # dict comprehension

# By contrast, the equivalent use of map only returns an iterator!
map(lambda n: n**2, numbers)
list( map(lambda n: n**2, numbers)) # forces iterator to produce all values

# The following generator expression is equivalent to the above call to map;
# thus it returns an iterator (note the parentheses - but it's not a tuple!)
(n**2 for n in numbers)

squares = (n**2 for n in numbers)   # iterator created
next(squares)                       # first square value returned
list(squares)                       # explicit list exhaustively generated
for n in squares: print(n, end=' ') # all values generated and printed

# Equivalent generator function
def squares_of(numbers):
    for n in numbers:
        yield n**2

for n in squares_of(numbers): print(n, end=' ')

sqg = squares_of(numbers)           # iterator created
next(sqg)                           # first square value returned
# ...
for n in range(4): print( next(sqg), end=' ') # more values


# Sum() takes a sequence (iterable) of numbers as argument, or an iterator!
# The iterator can be created by map, a generator expression, or a generator.
sum( [1,4,9,16,25,36,49,64] )
sum( {1,4,9,16,25,36,49,64} )
sum( map(lambda n: n**2, numbers) )
sum( (n**2 for n in numbers) )
sum( squares_of(numbers) )
# Note that, when there is only one argument to the calling function, the
# parentheses around the generator expression can be omitted:
sum(n**2 for n in numbers)


# Generators are very powerful programming constructs. They allow you to write
# streaming code with fewer intermediate variables and data structures, they
# are memory and CPU efficient, and typically require less code.
#
# So why do we need iterators if generators are so much simpler and better?
# Whenever we already have a class, and we need to provide access to its data!
# In the above, Fib should just be a generator/function but Deck (of cards)
# must be a class. Other examples include all abstract data structures e.g.,
# Stack, Queue, etc. A Binary Search Tree class can (and should) implement
# all traversal operations as iterators! (default being in-order traversal)


# Rule of thumb: whenever you have (imperative style) code similar to the
# following LoopingFunction, replace it with IterFunction:
#
#   def Loop_XFunction(...):          def Iter_XFunction(...):
#      result = []                        for ... in ... :
#      for ... in ... :                       yield x
#          result.append( x )
#      return result
#
# Their usage e.g., in a 'for' loop, is exactly the same of course. Then, 
# if you really need an explicit list structure in the end, just do this:
#    list( Iter_XFunction() )



################################
##
##  ASYNCHRONOUS GENERATORS [v3.6]
##


# Python now uses asynchronous coroutines instead of threads. Asynchronous
# coroutines are implemented as an extension to generators, with the benefits
# of using less memory and being easier to start, to use, and to maintain,
# than traditional threads. For details see the Coroutines and Asynchronous
# Coroutines section in 13. Threads and Concurrency. 

##
##  END
##

