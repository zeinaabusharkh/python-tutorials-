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
##  01. Introduction to Python
##  02. Sequences and Collections: generic data structures (and algorithms)
#                                  list, tuple, dictionary, set; and more...
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
###   02. SEQUENCES AND COLLECTIONS
###



################################
##
##  LISTS
##


# List class, implemented as a dynamic array - mutable of course
# (uses exponential over-allocation, a bit like ArrayList in Java).
l = ['one', 'two', 'three']
l
type(l)                             # 'list' object
isinstance(l, list)                 # checking the type

l.append("four")                    # appending
l * 2                               # repetition
l = l + ["five", "six"]             # concatenation
['zero'] + l                        # appending at front
ll = l[:]                           # list copy

l2 = l.copy()                       # many classes implement copy / deepcopy
l3 = list(l)                        # same (like copy constructor)

# Careful, there is no checking: list = [1,2,3] destroys the class!
# It works because a "class name" is just a reference to an object (instance
# of the 'class' class!) and references can be changed...


# Generic containers and sequences (only contains references anyway!)
lst = [1, 3.5, "hi", 2-3j, 'wow', False, 0xFFFF, ]   
print(lst)                          # (trailing comma is ok too)

a,b,c,d,e,f,g = 1, 3.5, 'hi', (2-3j), 'wow', False, 65535
[ a,b,c,d,e,f,g ]

for item in lst:                    # 'for' loop needs an iterable e.g., list
    print(item, '\t-> ', type(item))# (cf. Iterators and Generators section)


# Nested lists and indexing
nst = [1, [3.5, "hi", 2-3j, ['nothing', False]], 0xFFFF]
len(nst)
nst[1]
nst[1][-1][0]

# Multi-dimensional 'arrays' e.g., matrices
mtx = [ [11, 12, 13],
        [21, 22, 23],               # 1 line or multiple lines (rows) for
        [31, 32, 33] ]              # clarity's sake (bracket delimiters)
mtx[1][2]

# note: use NumPy module for really fast array/matrix and other math functions!


# List indexing and slicing (like with strings, other containers/sequences)
l[2]
l[2:4]
l[3] = "none"                       # replacing one item
print(l)
l[2:4] = [' 3 ', ' 4 ']             # replacing a slice! (multiple items)
del l[-1]

lx = l * 2
lx[2:6] = "oops"                    # string (implicitly) as list!
list("oops")                        # explicit conversion
lx[2:6] = ["oops"]
lx[1:3] = [1,2,3,4,5]
lx[0:4] = []                        # same as del lx[0:4]
lx[1] = ['a', 'aa', 'aaa']          # one item replaced by nested list!
lx[:] = []                          # clear the list? yes but same as: lx=[]


# List comparison (recursive)
[1, 2, 3] < [1, 2, 4]               # works with lists, tuples ...
(1, 2, 3) < (1, 2, 3, 4)            # (but not with dictionaries)
[1, 2, 3] == [1.0, 4/2, 2*1.5]
[1, ['a', 'b'], 3] < [1, ['x', 'y'], -2]

l2 = l[:]
l == l2                             # same items (compares values)
l is l2                             # different object (compares references)


# More list operations
nl = [0,1,2,3,4]
nl.append(5)                        # appending one item at a time
nl.extend([6,7,8])                  # appending multiple items (like +)
nl.insert(4,8)                      # inserting at position (given index)
print(nl)

rl = nl.copy()                      # same as nl[:]
rl.reverse()                        # reversing in place, vs. reversed(nl)
sl = sorted(rl)                     # new sorted list
print(nl, rl, sl, sep='\n')
rl.sort()                           # sorting in place

rl.pop(3)                           # removing at position (4th item here)
rl.remove(7)                        # removing a given value (int 7 here)
#rl.remove(77)                      # ValueError: x not in list
print(rl)
rl.count(4)                         # number of items with value 4


# References again
a = [1, 2, 3]                       # 'a' reference to a 'list' object
b = a                               # 'b' another reference to the same
a.append(4)                         # list object modified
print(b)
b = a[:]                            # now 'b' is copy of 'a' (diff object) 
a.append(5)
print(a, 'vs', b)


# List as Stack (fast)
nl.append(6)                        # push: same as append (at the end) 
nl.pop()                            # pop: delete and return last item
nl[-1]                              # top: return last item

# List as Queue (slow)
nl.append(8)                        # enqueue: same as append (at the end)
nl.pop(0)                           # dequeue: delete/pop the first item

# Better queue (fast)
from collections import deque
q = deque(["Eric", "John", "Mike"])
q.append("Toby")                    # enqueue: same as append
q.popleft()                         # dequeue: delete/pop left (first) item
print(q)

enq = deque.append                  # one can even create function aliases
deq = deque.popleft
deq(q) ; enq(q,'Zara')


# Many more collections are available e.g., min heap (for priority queue) via
# heapq algorithms, plus utilities such as merge, nlargest, nsmallest...

from heapq import merge
# list(merge([1,3,5,7], [0,2,4,8])) # merge is a generator (see later section)

def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = merge_sort( a[:mid] )
    right = merge_sort( a[mid:] )
    return list(merge( left, right))

merge_sort([3, 4, 1, 9, 0, 8, 6, 2, 7, 5])

def merge_sort(a):
    if len(a) <= 1: return a
    return merge(merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])) # [FP]



################################
##
##  TUPLES
##


# Tuple class, a lightweight, immutable list. Fewer methods (since read-only)
# but much better performance-wise. Used a lot *inside* Python... [FP]
t = (1,2,3)
type(t)                             # 'tuple' object

u = 2, 4, 6                         # packing (parentheses are optional)
print(u)
t + u[1:2]                          # new tuple, via slicing + concatenation

x,y,z = t                           # unpacking (num of values must match)

for item in t:                      # tuples are also iterables
    print(item)

a, b = 1, 2                         # parallel assignment again
a, b = (1,2)                        # same - actually implemented as tuple
tu = (1, 2)                         # packing followed by unpacking
a, b = tu                           # (so functions can return multiple
                                    #  values! - cf. Functions section)

#t[1] = "one"                       # TypeError: no item assignment

u = 2,                              # singleton (comma needed, else 'int')
u = ('two',)                        # singleton (comma, else 'string')


# Conversion
lt = list(t)                        # list constructor (with tuple arg)
lt[1] = -2 ; lt.append(4)
tt = tuple(lt)                      # tuple constructor (with list arg)


# Example
pA , pB = (2,7) , (5,-1)            # two 2D points (immutable!)
pA[0] * pB[0] + pA[1] * pB[1]       # dot product

# More elegant with named tuples i.e., tuples with fields
from collections import namedtuple
point = namedtuple('point', ['x', 'y']) # 2D point struct (opt: verbose=True)

pA, pB = point(2,7) , point(5,-1)   # same syntax as when using a point class
pA.x * pB.x + pA.y * pB.y           # now accessing fields/attributes by name!

px, py = pA                         # unpack like a regular tuple
px == pA.x

#pA.x = 5                           # AttributeError: can't set attribute


# A general design rule is that "tuples have structure, lists have order".
# So tuples are used as heterogeneous data structures containing unmodifiable
# data e.g., (name, ID, birthdate) for a person's record or (X,Y) for a point
# coordinates. Lists are homogeneous more often than not e.g., list of names,
# of ID's, shopping list (of items), etc. Yes Python's list is generic (it can
# store anything) but that is really a consequence of having dynamic types...



################################
##
##  DICTIONARIES
##


# Dictionary class, a.k.a. associative array, map, hash table... A dictionary
# stores key-value pairs e.g.
d = { 'fr': "France", 'uk': "United Kingdom", 'it':"???" }
type(d)                             # 'dict' object
print(d)                            # actual order depends on hashing

#d[1]                               # KeyError: only key indexing allowed
d['fr']
d.keys()
d.values()
d.items()

for k in d: print(k)                # dictionaries are iterables

for k in d.keys(): print(k)         # same, iterating over dictionary keys

for v in d.values(): print(v)       # iterating over dictionary values

for k in d: print(d[k])             # same, getting values from the keys


d['it'] = 'Italy'                   # replacing value for given key
d['ch'] = "Switzerland"             # adding new key-value pair
del d['uk']                         # removing key-value pair

d[42] = 'yes'                       # adding key 42 (not an index)


# Any immutable object can be used as a key e.g. int, float, string, tuple...
d[(1,2,3)] = 'a tuple key!' 
d['flag'] = ["red","white","blue"]
print(d)

# Hashing is built-in for all Python immutable classes
hash(1)
hash('1')                           # string hash - function or method
'1'.__hash__()                      # (cf. Classes and OOP section)
hash((1))


points = { 'A': (2,5), 'B': (4,1), 'C': (-2,0), 'P': point(7,11) }
print(points.keys())                # iterator (cf. Iterator section)
print(list(points.keys()))          # now a list is explicitly generated
points['B']
points['A'][0]
points['P'].x
for k in points.keys(): print(points[k])


# Default dictionary is not immutable, not ordered...

# Ordered dictionary, where items are stored in order of insertion
from collections import OrderedDict
od = OrderedDict([ ('z', 26), ('g', 7), ('k', 11) ])
print(od)

# Immutable dictionary: frozendict, available as third-party module  (not
# included in Python because the demand is low, according to the designers)



################################
##
##  SETS
##


# Set class, unordered collection of unique items (must be hashable objects)
s1 = { "France", "United Kingdom", "Italy", "Germany" }
type(s1)

s2 = set([1,4,7,9,4,8,2,1,4,9,8,1,4,7,2,4,8,1,4]) # set created from a list
print(s2)                           # each item is now unique

# note: we can use set to remove duplicates! e.g. alist = list(set(alist))


for item in s1: print(item)         # sets are iterables too  

s3, s4 = set("pecan"), set("pie")
s3 & s4                             # intersection -> {'p', 'e'}
s3.intersection(s4)                 # same
s3 | s4                             # union: {'i','n','c','a','e','p'}
s3 - s4                             # difference: {'c', 'a', 'n'}
s3 ^ s4                             # symmetric diff: {'i', 'n', 'c', 'a'}
s3 &= s4                            # intersection update: s3 is {'p','e'}
s3 <= s4                            # subset
s3.issubset(s4)
s3 |= s4                            # update -> s3 is {'i', 'p', 'e'}
s3.update(s4)


# Frozen set, immutable version [FP]
s5 = frozenset(s4)
s4.add('x')
print(s4, 'vs', s5)                 # {'i', 'p', 'x', 'e'} vs frozenset...

#s5.add('x')                        # AttributeError: no attribute 'add'


# Sequence: a collection data type that supports the membership operator 'in',
# the size function 'len()', and is iterable e.g., list, tuple, dict, set...



################################
##
##  OTHER COLLECTIONS
##


# collections module: Counter (bag), OrderedDict, defaultdict, UserDict,
# deque, ChainMap, Container, Hashable, Sized, Mapping, MutableMapping, ...
# Iterable, Iterator, Generator (cf. later sections)

from collections import Counter

c = Counter('abcdeabcdabcaba')      # count elements from a string
c['a']                              # count of letter 'a'
c.most_common(3)                    # three most common elements
sorted(c)                           # list all unique elements
''.join(sorted(c.elements()))       # list elements with repetitions



################################
##
##  LISP/SCHEME EMULATION
##


# To get Lisp-style linked lists, one can emulate cons cells using tuples:
lisp_list = ("like",  ("this",  ("example", None) ) )

def car(lst): return lst[0]
def cdr(lst): return lst[1]
def cons(atm,lst): return (atm, lst)

car( cdr( lisp_list))               # lisp: (car (cdr lisp_list))
cons('just', lisp_list)             # lisp: (cons 'just' lisp_list)

# etc. (Writing a Lisp interpreter in Python is left as an exercise.)



##
##  END
##
