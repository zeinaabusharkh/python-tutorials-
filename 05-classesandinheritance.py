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
##  05. Classes and Inheritance: attributes, functions, scope, inheritance,
##            reflection, abstract classes, multiple inheritance, interfaces
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
###   05. CLASSES AND INHERITANCE
###



################################
##
##  CLASSES AND ATTRIBUTES
##


# Class definition
class Stack(object):                # subclass of the 'object' class (default)

    """A well-known data structure
         ...
    """                             # doc string

    verbose = False                 # (static) class variable
    counter = 0

    def __init__(self):             # initializer (calls __new__ constructor)
        self.items = []             # instance variable (self = this)
        Stack.counter += 1          # accessing the class variable
    
    def __del__(self):              # Python has garbage collection...
        Stack.counter -= 1

    def push(self, x):
        self.items.append(x)        # accessing instance variable

    def pop(self):
        if not(self.isempty()):     # calling another function/method
            x = self.items[-1]
            del self.items[-1]
            return x
        else:
            print("cannot pop an empty stack")
            return None

    def isempty(self):
        return not self.items       # or: len(self.items) == 0
                                    # or (ugly): self.items == []
    def print(self):
        print(self.items)           # (see also __str__ function)

    def count():                    # class function (static method)
        return Stack.counter

    def Stack():
        print("static class function - NOT a constructor!")

s = Stack()                         # instance created (calls __init__)
s.push(2)                           # function (method) call  [OO]
s.push(4)
Stack.push(s,6)                     # same, as pure function call!
type(Stack.push)                    # note: compare to e.g., math.pow(2,5)

s.print()
s.items                             # no data hiding! (simulated only)

s.pop()
Stack.pop(s)

Stack.verbose                       # class variable
s.verbose                           # shared by all instances

Stack.count()                       # calling the class function
Stack.counter
s.counter


s2 = Stack() ; s3 = Stack()
Stack.count()                       # 3 stack objects now
del s2
Stack.count()                       # 2 left
s3 = "not a stack anymore"
Stack.count()                       # 1 only (garbage collection!)
s = Stack()                         # now 1 or 2?

# note: del() does not necessarily call __del__(); it simply decrements the
# object’s reference count, and if this reaches zero __del__() is called.

# s.count()                         # error, same as Stack.count(s)
s.isempty()                         # implicit parameter
Stack.isempty(s)                    # same, explicit parameter
Stack.print(s)                      # same as s.print(), but
print(s)                            # Stack obj, need custom __str__

s.data = 'wow!'                     # new instance variable! created
s.data                              # dynamically (don't do that)



################################
##
##  STRUCT / RECORD
##


# A class with no method is essentially a 'struct' (C style). But
# in Python we can use namedtuple instead (better).

class Employee: pass                # class with no variable, no function

john = Employee()
john.name = 'John Doe'
john.dept = 'business'
john.salary = 1000                  # struct now has name, dept, salary



################################
##
##  SCOPE (again)
##


v = 1                               # global variable (script scope)

class TScope(object):

    v = 2                           # class variable / attribute
    
    def __init__(self):
        self.v = 3                  # member var / object attribute

    def scopes(self):
        v = 4                       # local var (function/method)
        
        print("  global v:",  globals()['v'])
        print("    locals:",   locals()['v'])
        print("vars(self):", vars(self)['v'])
        
        print("   class v:", TScope.v) # or just v, if no local var
        print("  member v:",   self.v)
        print("   local v:",        v)

TScope().scopes()

print(TScope.v)                     # -> 2 (class variable)
print(TScope().v)                   # -> 3 (attribute of new object)



################################
##
##  ATTRIBUTE ACCESS
##


# Attributes and methods starting with an underscore are treated as 
# non-public ("protected"). Names starting with a double underscore are
# considered strictly private (Python mangles class name with method name
# in this case: obj.__var has actually the name _classname__var)

class PPPClass(object):
    def __init__(self):
        self.a   = 1                # "public" variable
        self._b  = 2                # non-"public" variable
        self.__c = 3                # "private" variable

    def __print(self):              # "private" method
        print(self.a, self._b, self.__c)

    def print(self):                # "public" method (calling the above)
        self.__print()

p = PPPClass()
p.a                                 # only visible attribute (cf. thumbnail)
p._b                                # accessible but not visible
# p.__c                             # error - not accessible
# p.__print()                       # (since the name has been mangled)
p.print()

dir(p)                              # reveal "hidden" variables and methods
p._PPPClass__c                      # now we can access the "private" variable
p._PPPClass__print()                # and call the "private" method (!)


# Note: Python is designed to be *simple*, interpreted, and then scripts are
# distributed as source 98.5% of the time... Then, if users have the source
# code, they can access/change anything they like! Hence there is no point
# declaring something "private", when users can make it "public"! Python has
# encapsulation/classes and polymorphism/inheritance but no data hiding.
# (Besides, implementing access control - private vs. public vs. protected -
# implies a lot of complexity  as well as performance overhead at runtime.)



################################
##
##  REFLECTION
##


# Special attributes again
s.__dict__                          # class-defined attributes
s.__class__                         # a class object
s.__class__.__name__                # name of class
s.__class__.__doc__                 # documentation string
s.push.__name__                     # likewise, name of method

dir(s)                              # get names of all attributes and methods
                                    # incl. __init__(), __hash__(), __eq__()
s.__dir__()                         # ... __class__, __doc__, ...

'count' in dir(s)                   # check if a method exists (by name)


# Special methods
# __init__(self [, args]):          constructor
# __del__(self):                    del() - destructor (optional, due to GC)
# x.__len__()                       len(x) - length of x (list, string, ...)
# func.__call__(x)                  func(x) - function call 
# __str__(self):                    string representation returned by str()

class Class2Print(object):
    __head, __tail = '< ', ' >'
    def __init__(self,data):
        self.__data = data
    
    def __str__(self):
        return self.__head + str(self.__data) + self.__tail
        # or   repr(self.__head + str(self.__data) + self.__tail)

Class2Print(12345)                  # a Class2Print object
print(Class2Print(12345))           # output from __str__()


# Defining standard operators (not "overloading"! more like interfaces)
# a + b   same as  a.__add__(b)
# a += c  same as  a.__iadd__(c)
# a[3]    same as  a.__getitem__(3)
# a[3]=1  same as  a.__setitem__(3,1)
# a == b  same as  a.__eq__(b)          - cf. comparable interface in Java
# a != b  same as  a.__ne__(b)
# ...


# note: repr vs. str - both functions return a string for printing, but:
str(123)                            # string '123'
repr(123)                           # same - but now:
str('Python')                       # -> 'Python'
repr('Python')                      # vs. "'Python'"

# The __str__ function (str) converts an object into a human-readable form
# i.e. what you, as a user, might wish to see when you print an object out.
# The __repr__ function (also repr) converts an object into a string which
# you, as a programmer, might wish to have to recreate the object e.g.
# using the eval() function.
eval(repr('Python'))
#eval(str('Python'))                # NameError: 'Python' not defined
import datetime
now = datetime.datetime.now()       # now compare:
str(now)                            # -> '2018-03-01 15:52:15.760365'
repr(now)                           # -> code to create the above!
# -> 'datetime.datetime(2018, 3, 1, 15, 52, 15, 760365)'
print(eval(repr(now)))

# note: Python 2 had the backquote (like Lisp/Scheme!) as a shortcut for
# repr i.e. you could write print(" answer = `f()` ") where f() would be
# evaluated, so the output might be e.g. answer = 42
# In Python 3 you can do the same with: print(" answer = " + repr(f()))
# In v3.6 onward you can use formatted strings: print(f'answer = {f()}')
# so basically curly brackets have replaced the Lisp-like backquotes...

# note also that the print() function uses __str__, if defined, and __repr__
# otherwise. The interpreter uses __repr__ only.



################################
##
##  OBJECT-ORIENTED PROGRAMMING
##


# Methods vs. functions, classes vs. modules ...

import math                         # math.py module
math.pi                             # constant
math.gcd(15,40)                     # function

class math(object):                 # math class (oops, no more module...)
    pi = 3.1415                     # constant
    def gcd(a, b):                  # function
        while a != 0: a, b = b%a, a
        return b
math.pi                             # class or module? same syntax!
math.gcd(15,40)


# list class
l = [1,2,3,4]
l.append(5)                         # OO style, equivalent to
list.append(l,5)                    # a function call


import collections                  # collections.py module
q = collections.deque()             # deque class

q.clear()                           # OO style, equivalent to
collections.deque.clear(q)          # a function call

collections                         # module    |
collections.deque                   # class     |  4 levels of encapsulation
collections.deque.clear             # function  |  (all are refs to objects)
collections.deque.clear.__name__    # object    V


# __code__ + see above OO vs. FP style ...



################################
##
##  CLASS INHERITANCE
##


class PeekStack(Stack):
    "A stack where one can peek at inferior items"

    def peek(self, n):
        "peek(0) returns top, peek(1) returns item below that; etc."
        size = len(self.items)
        if 0 <= n < size:
            return self.items[size-1-n]

y = PeekStack()                     # calls the inherited constructor
y.push('a')
y.push('b')                         # inherited push method
y.push('c')
y.peek(1)                           # subclass method
y.print()


# Checking the class hierarchy
isinstance(y,PeekStack)
isinstance(y,Stack)                 # both True

issubclass(PeekStack, Stack)
issubclass(bool, int)               # both True
issubclass(float, complex)          # False

x = PeekStack()
if x.__class__ is y.__class__: print('same class')

if x.__class__.__name__ is y.__class__.__name__: print('same class')


# Subclassing / inheritance
class LimitedStack(PeekStack):
    "A stack with limit on stack size"

    def __init__(self, limit):
        super().__init__()          # call the base class constructor
                                    # alt: PeekStack.__init__(self)
        self.limit = limit          # add a new member variable

    def push(self, x):
        if len(self.items) < self.limit:
            super().push(x)         # call the base class method
        else:
            print("stop pushing!")

    def __len__(self):              # for len()
        return len(self.items)

    def __str__(self):              # for print()
        return str(self.items)      # or: "{}".format(self.items)

z = LimitedStack(3)
z.push(1)
z.push(2)
z.push(3)
z.items
z.push(4)
len(z)
z.items
print(z)



################################
##
##  MULTIPLE INHERITANCE
##


# Multiple inheritance is available in Python (of course).
# The 'diamond problem' is solved via an order of precedence (LTR).

class XFather(object):
    def __init__(self):
        print("father side")
    def test(self):
        print("daddy says hi")      #     object
                                    #    /      \
class XMother(object):              #  XFather  XMother
    def __init__(self):             #    \      /
        print("mother side")        #     XChild
    def test(self):
        print("mommy says hi")
    def test3(self):
        print("mommy only")

XMother().test()


class XChild(XFather, XMother):     # order is essential, defines inheritance
    def __init__(self):
        super().__init__()          # super() same as super(XChild, self)
        print("child here")
    def test2(self):
        super().test()
        print("kiddy waves hello")
    def test3(self):
        super().test3()
        print("kiddy again")
        
c = XChild()
c.test()
c.test2()
c.test3()



################################
##
##  ABSTRACT CLASSES
##


import abc

# Abstract base class
class Shape(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self.__name = ''
        print("new shape built")

    def set_name(self,name):        # concrete method: inherit or replace
        self.__name = name

    def name(self):
        return self.__name

    @abc.abstractmethod             # decorator - modifies the function!
    def draw(self):                 # denotes an abstract method: must be
        return                      # implemented in concrete subclasses

# note: Decorators are like functions (defined elsewhere) that modify the
# behavior of the "decorated" function (cf. ?? section).
# This is very different from e.g., @override in Java, which is just a
# keyword instructing the compiler to perform some extra checking.
# The Decorator Pattern has become one of the classic OO Patterns...

# Concrete subclass
class Cube(Shape):

    def __init__(self):
        super().__init__()
        print("and it's a cube")

    def draw(self):
        print("See me? I'm a", self.__class__.__name__)

class Unknown(Shape):
    "fails to implement the abstract draw method" 

# sh = Shape()                      # cannot instantiate abstract class
cu = Cube()
cu.draw()
# un = Unknown()                    # cannot instantiate abstract subclass



################################
##
##  INTERFACES IN PYTHON
##


# Interfaces are all implicit in Python i.e., there is no explicit interface
# syntax (as in Java). For a Python class to implement an interface means to
# define one or more required functions - that's it!
#
# For any object to be 'printable' in Python i.e., so that print() will work
# with it, its class only needs to implement the __str__() function (and make
# it return a string object comprising the desired attributes). Almost every
# built-in Python class is printable.
# For any object to be 'comparable' its class must implement __eq__() so that
# x == y will work as expected (also __ne__() for difference, x != y).
#
# To make any object 'countable', its class needs to implement the __len__()
# function (and make it return an integer). Many Python classes are countable
# e.g., all containers / sequences (list, dict... str...)
# To be a container / sequence, a class must implement __contains__() so it
# will work with membership functions e.g., if x in X: ...
#
# For a class to be 'hashable' i.e., so it will work with maps and hash tables
# et al, it must implement the __hash__() function. Almost every Python class
# is hashable (if it makes sense).
# To make any object 'callable', like a function, its class needs to implement
# the __call__() function (the body of which is executed when a call is made).
#
# For any object to be an 'iterable', its class must implement the __iter__()
# function (to return an iterator, which can be done simply using iter() for
# example). Python classes such as range, zip, and enumerate are iterables, so
# are all containers / sequences...
# Likewise an iterator is a class that implements a __next__() function...
# (See Iterators and Generators section).
#
# To implement an interface in Python means to fully and properly implement
# the desired functions and behaviour: it is the programmer's responsibility
# to do so (Python will not check). If coded correctly, then it "just works".
# (This is known as Python "duck typing": if your code "looks like a duck and
# quacks like a duck, it's a duck!")
#
# Note that, in addition to the above examples, Python uses interfaces for:
# Classifier, Clustering, Converter, Distribution, Evaluation, ... Regression,
# Serialization, and many more.
# (See also: Python design by Contract @ http://pythondbc.codeplex.com/)



##
##  END
##
