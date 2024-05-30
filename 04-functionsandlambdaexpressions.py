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
##  04. Functions and Lambda Expressions: function objects, doc, attributes,
##                      scope, default args and keywords, lambda expressions
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
###   04. FUNCTIONS AND LAMBDA EXPRESSIONS
###



################################
##
##  FUNCTIONS
##


def welcome():
    print("Welcome to Python!")     # return statement is optional

# Functions are objects! (data in Python)
welcome                             # reference / variable: function welcome
type( welcome )                     # object of 'function' class

welcome()                           # calling the function (w/ parentheses)

#welcome = 3                        # careful again - function ref is gone!
#welcome()                          # TypeError: 'int' is not callable

def vwelcome(version):              # type inference for args too!
    print("Welcome to Python", version)
    print(type(version))            # function body/block is indented
    return version

vwelcome(3)                         # returns an int
print(welcome())                    # returns 'None' (no value)


def gcd(a, b):
    "greatest common divisor"       # doc string (also used in thumbnail)
    while a != 0:
        a, b = b%a, a               # parallel assignments (via a tuple)
    return b

gcd(12,20)

# Fibonacci numbers again
def fibonacci(n):
    """Prints all Fibonacci numbers up to n.

Some lengthy story about as Leonardo Fibonacci of Pisa, who popularized the
use of Arabic numerals in Europe in the 13th century, and made many original
contributions to algebra, geometry, number theory, etc. and also how he went
about counting rabbits and thus discovered the so-called Fibonacci series...
"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b               # parallel assignments (via a tuple)


def sqpair(x):                      # returning multiple values! (via tuple)
    return x, x**2

value, square = sqpair(4)           # unpacking values from returned tuple

quo, rem = divmod(22, 3)            # function returning 2 values (unpacked)
print(quo, 'and', rem)
divresult = divmod(22, 3)           # same, as tuple (no unpacking)

def CubicRoots(x1,x2,x3):           # solve x**3 + a * x**2 + b * x + c == 0
    return -(x1+x2+x3), x1*x2+x2*x3+x1*x3, -(x1*x2*x3) # (not)


# Is Python call-by-value or call-by-reference (C++ style)? Neither! The most
# accurate way to describe it is "call-by-object-reference".
def plural(noun): 
    return noun+'s'                 # noun is a local var/ref. to arg object
pet = 'cat'                         # pet is a ref. to string object ("cat")
plural(pet)                         # noun is pet, they refer to same object

# note: Everything so far as global scope. 'pet' and 'plural' are references
# to string and function objects, resp. - defined at the top level. However,
# 'noun' is defined in the function block hence its scope is limited to it;
# it is a local reference to the same string object as pet (in this case).


# 'def' is dynamic i.e., it can be evaluated at runtime! For example:
if 2**10 is 1024:
    def dg(n):
        print(n+2)
else:
    def dg(n):
        print(n*2)
dg(5)

if 2**10 is 1024:
    dg = lambda n: print(n+2)       # equivalent def using lambda expression
else:
    dg = lambda n: print(n*2)       # (see further below)


# Nested functions, good for helper functions, also to protect functions e.g.
# from changes, since their scope is only that of the enclosing function.
def nse(n):
    def sprint(s):                  # defining function as 'data' - their
        print('*', s, '*')          # scope is that of the enclosing block
    def iseven(x):
        return x % 2 == 0
    sprint( iseven(n))              # calling two local functions



################################
##
##  FUNCTION ATTRIBUTES
##


# Specific object attributes follow the "double underscore" syntax e.g., name:
gcd.__name__
f = gcd                             # alias (another reference)
f.__name__
f(12,20)

# Object attributes can also be retrieved programmatically (reflection)
getattr(f, '__name__')


# Documentation string attribute, implementation
gcd.__doc__
str.__doc__

# Purposes: (1) source code doc + online documentation via __doc__
# (2) generated documentation via e.g., HappyDoc (like Javadoc)
# (3) ballon help in the shell (e.g., in IDLE, also other IDE's)
# (4) automated code testing! (cf. Meta-programming section)

def myf(x):
    """my "mystery" function of x (!)

    long description bla bla bla ...
    """
    pass                            # place holder (means: to be coded later)

print(myf.__doc__)

gcd.__code__                        # body of the function, as defined
                                    # (cf. also lambda expressions)


# Instances of any class can be made callable by defining a __call__() method
type(gcd)
gcd.__call__                        # function has __call__()
gcd.__call__(10,35)                 # same as gcd(10,35)

class C:
    def __call__(self): print('did you call me?') # (cf. Class section...)
c = C()
c()


# Introspection! (cf. also Iterators section and the Dispatcher example)
mlist = [1,2,3,4]
mname = "pop"                       # retrieving function code given an
mpop = getattr(mlist,mname)         # instance of the class (list object)
print(mpop)                         # then calling the function on it
mpop()                              # (can use dir() to find names...)
print(mlist)
 


################################
##
##  FUNCTION SCOPE
##


# Python's scoping rule is a straight search from the inner to the outer scope
# and again and again... Eventually it reaches script level i.e. global scope.

code = 111                          # global variable (script level)

def gff():
    locv = 88                       # local variable (function level)
    print("code=", code)            # global var, found in outer scope
    print("locv=", locv)

# locals() and globals() return a dict of variable names and values, defined
# within the scope where the function is called, and at script level, resp.

globals() is locals()               # same at the script/module level
print(globals().keys())             # show all objects/refs defined so far

def pgl():
    x, y = 3, "qewrqerrq"
    print(locals())
    return globals() is locals()    # local scope is not global scope
pgl()


def gfg():
    lovc = 88
    code = 421                      # local var, hides the global var
    print("code=",code)
    print("local variables:", locals())
    print("global 'code':", globals()['code'])

def ggg():
    global code                     # needed: which 'code' var(?)
    code *= 2                       # else Error: ref before assignment
    print(code)

def ghg(): 
    code = 111
    def ghg2():
        nonlocal code 	            # nonlocal needed to refer to a
        code += 1		    # previously bound variable in the
        print(code)	            # nearest outer scope (excl. globals)
    ghg2()

def ghh(): 
    code = 111
    def ghh2():
        global code 	            # global refers to script-level,
        code += 1		    # regardless of how many scope levels 
        print(code)	            # are nested within one another
    ghh2()

fvar = 0
def f1():                           # nested function scope example
    fvar = 1                        # (similar to nested block scope)
    def f2():
        def f3():                # comment this line, then same in f2, f1
            return fvar             # scope: f3 -> f2 -> f1 -> script/global
        return f3()
    return f2()



################################
##
##  DEFAULT/KEYWORD ARGUMENTS
##


# Default / keyword arguments
def dwelcome(version=3):
    print("Welcome to Python", version)
    return version

dwelcome()
dwelcome(4)
dwelcome(version=5)

def daf(x, y=3, s="default"): print(x, y, s)

daf(4)
daf(4, 5)
daf(4, 5, "hello")                  # override defaults, in order
daf(8, s="ok")
daf(8, s="ok", y=777)               # with keywords, in any order


# Variable-length argument list
def concatz(separator, args):       # requires a list of args (inconvenient)
    return separator.join(args)

concatz('/', ['red','green','blue'])

def concatx(separator, *args):      # allows variable number of args
    return separator.join(args)

concatx('/','red','green','blue')   # first arg is the separator

# implementation note: f(*args) replaces apply(f,args) in Python 3

def concat(*args, separator="/"):   # all args absorbed by *args thus
    return separator.join(args)     # separator keyword is necessary

concat('.','red','green','blue')  
concat('red','green','blue', separator=".")


# Setting the default value
da = 5
def dff(arg=da):                    # default set the first time
    print(arg)

dff()
dff(8)
da = 10                             # default not changed - unless the above
dff()                               # def statement is evaluated again!

# note: It is often expected that a function call creates new objects for
# default values. This is not the case. Default values are created exactly
# once, when the function is defined.

def atl(itm, lst=[]):
    lst.append(itm)                 # default value updated/shared
    return lst

print(atl(1)) ; print(atl(2)) ; print(atl(3))

def atll(itm, lst=None):
    if lst is None:
        lst = []
    lst.append(itm)                 # default value not shared
    return lst



################################
##
##  TYPE ANNOTATIONS [v3.6]
##


# Standard version, where no type is specified:
def greeting(name):
    print('Hello', name)
# So the argument passed could be anything:
greeting('Sam')
greeting(1234)

# A better version could rely on some operation to raise an exception if the
# arg type is not supported e.g., string concatenation with a non-string arg
# (note this is better than explicitly using isinstance)
def greeting(name):
    print('Hello ' + name)
greeting('Sam')                     # fine; then a non-string argument will
#greeting(1234)                     # cause a TypeError: must be str, not int

# Using annotations, the type of function arguments and/or its return values
# can be specified. The syntax is similar to Haskell and other languages [FP]:   
def greeting(name: str) -> str:
    print('Hello', name)
# The argument passed could still be anything; type is NOT checked at runtime!
greeting('Sam')
greeting(1234)
# However, code using type annotations is clearer (shows intent), and it can
# now be checked by a separate (off-line) type checker, such as within an
# editor or IDE, or a compiler(!) etc.


# Function type annotations are (only) stored in the __annotations__ attribute:
greeting.__annotations__


# Type annotations are also available for variables [v3.6] e.g.
var = 3
# can now be written as follows
var: int = 3
# Type annotations also allow 'declaring' a variable without initializing it.
surname: str

# This again improves clarity even though NO type checking occurs at runtime.
count: int = 'oops'
surname = 1+2j



################################
##
##  LAMBDA EXPRESSIONS
##


# Lambda expressions are anonymous functions i.e., not bound to an identifier
# (from Lambda Calculus, the formal logic used in CS to express computation).
# Fully supported in Functional Programming, but only partially supported in
# languages such as Python, and now Java 8, C++11, C#, JavaScript, etc.)
# Syntax differences e.g., no parentheses around args, implicit return,
# if/else... in Python pretty much limited to single line body.

def odd(x): return x % 2 != 0       # using function def syntax
odd
odd (5)

oddfun = odd                        # another reference to the same function
oddfun(7)

oddl = lambda x: x % 2 != 0         # same using (anonymous) lambda expression
oddl                                # now bound to an identifier (a name)
oddl(5)

# note: since functions are just objects, it makes sense that we can use
# anonymous functions just like we can use anonymous objects (without ref.)


(lambda x: x % 2 != 0) (5)          # same, without any reference

if 2**10 is 1024:
    dg = lambda n: print(n+2)       # prev. example again, using lambda expr.     
else:
    dg = lambda n: print(n*2)


# In Python, functions and lambda expressions are defined just like any other
# "first class" object, and can be passed as function arguments, returned as
# the value of function calls, stored in variables, lists, etc. 

def testingf(f, x):                 # function/lambda passed as argument
    print(f, 'applied to', x, 'is', f(x) )
    if f(x): print('ok')

testingf(odd, 5)                    # <function odd ...> applied to 5
testingf(lambda x: x % 2 != 0, 5)   # <function <lambda> ...>

def execf(command = lambda: None, *args):  # apply given command to args
    return command(*args)           # (cf. Higher-Order Functions section)

execf()                             # default call does nothing
execf(lambda: print("Hi there!"))   # lambda expression with no arg
execf(odd, 5)                       # odd function, defined earlier
execf(lambda x: x%2 != 0, 8)        # lambda with 1 arg (odd)
execf(lambda x,y: x==y, 2,3)        # lambda with 2 args (equal)
execf(sum, [1,2,3,4])               # sum function with list arg

# Minimal GUI button demo (cf. Graphics and GUI Extensions for more examples)
# A button click causes the command i.e., given function or lambda expression,
# to be called and its code to be executed. Note the concise, obvious syntax!
# (This shows exactly why Java 8 adopted lambda expressions...)
import tkinter
class tkdemo(tkinter.Frame):
    def __init__(self):
        root = tkinter.Tk()
        tkinter.Frame.__init__(self,root)               # app window, has
        tkinter.Button(root,                            # one button
                       text = "Click me",               # with a label 
                       command = lambda: print("Hello") # and a function
                       ).pack()
        root.lift()
#tkdemo().mainloop()


# Syntax for conditional statements
def hilo(n):
    if n > 1000: return n/100       # imperative function style
    else: return n

hilo(12345)

def hilof(n):
    return n/100 if n > 1000 else n # functional programming style
                                    # (using lambda expression syntax)

(lambda n: n/100 if n > 1000 else n)(12345) # lambda style (cf. Comprehensions)

(lambda n: n > 1000 and n/100 or n) (123)   # logically equivalent alternative


def fact(n):                        # imperative function style
    if n == 1: return 1
    else: return n * fact(n-1)

def fact(n):                        # functional programming [FP] style
    return 1 if n == 1 else n * fact(n-1)


# For many more examples, see the Higher-Order Functions section.


# Example of a function that returns a function object
from math import log

def make_logB(base):                
    def logB(x): return log(x) / log(base) # ad hoc lambda expression created
    return logB                            # and returned as value

log2 = make_logB(2)                 # creating a log base 2 function
log2(1024)                          # and calling the function

def make_log(base):
    return lambda x: log(x) / log(base) # same with a lambda expr. (simpler)

make_logB(2) (1048576)              # create and call an anonymous function


# No function overloading in Python! (dynamic ref binding instead)
def fol(n): print(n+1)
fol(3)

def fol(n): print(n+2)              # dynamically (re)defines the function
def fol(n,p): print(n*p)            # same, not overloading!

fol(3,4)                            # 12, as expected
#fol(3)                             # TypeError: missing 1 required arg: 'p'

def fol(n,p=5): print(n*p)
fol(3)                              # 15, since only the second version exists


# Careful about overwriting again! e.g.:  sorted = lambda lst: sorted(lst)



# note: Functions and lambda expressions are examples of subroutines, where
# all code is executed sequentially / synchronously. Coroutines on the other
# hand are subroutines where code is executed concurrently / asynchronously.
# (See section 13. Threads and Concurrency.)



##
##  END
##
