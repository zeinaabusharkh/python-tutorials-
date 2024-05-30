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
##  09. Regular Expressions and Pattern Matching
##  10. Reflection and Meta-programming: reflection, dispatch, meta-classes,
##                          eval / exec, compiling code, automated testing
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##



###############################################################################
###
###   10. META PROGRAMMING IN PYTHON
###



################################
##
##  REFLECTION
##


# (2do: move from intro)



################################
##
##  SINGLE/MULTIPLE DISPATCHING
##


# Dispatcher pattern: use getattr() to retrieve from an object an attribute
# by name e.g., a method of that object or class, then call it!

aname = 'lower'
afunc = getattr(str, aname)         # named method of string class
afunc('I Am a Rock')
afunc = getattr(str, 'upper')       # same as str.upper
afunc('I Am a Rock')

# Example of a flexible plugin design using the dispatcher pattern:
class SavePlugin(object):
    """Plugin architecture for saving files in many formats."""

    def save_as_html(self, name):
        print("Saved HTML file", name + ".htm")

    def save_as_pdf(self,name):
        print("Saved PDF file", name + ".pdf")

    def save_as_rtf(self, name):
        print("Saved RTF file", name + ".rtf")

    def save_as_txt(self, name):
        print("Saved TEXT file", name + ".txt")

def save_file(name, ext = 'txt'):
    plugin = SavePlugin()
    getattr(plugin, 'save_as_' + ext, plugin.save_as_txt)(name)

save_file("report")
save_file("report", "pdf")
save_file("report", "xyz")          # no match, default is used



################################
##
##  META CLASSES
##


class NewClass(object):             # standard (manual) class definition
    attr = 100

NewClass = type('NewClass',         # programmatic class definition!
                (object,),          # super class(es)
                {'intattr' : 100})  # attribute(s)
nc = NewClass()
nc.intattr

type(nc)
nc.__class__
nc.__class__.__class__              # type = metaclass = class factory

NewChild = type('NewChild',         # subclass name
                (NewClass,),        # super class(es)
                {'listattr' : [],   # new attributes and functions/methods
                 'pratt': (lambda obj: print(obj.intattr, obj.listattr))})
ncc = NewChild()
ncc.listattr
ncc.pratt()


# see also getattr() examples earlier



################################
##
##  EVAL / EXEC / INTERPRETER
##


# Interpreting a Python expression string -- note that this is exactly what
# the Python interpreter does each time you type an expression at the prompt
# and press return, or when you run a Python script.
eval("1 + 2")

a,b = 1,2
eval('a + b')

bindings = {'a': 3, 'b': 4}         # dictionary of bindings
eval('a + b', bindings)

eval('f(a,b)', {'a': 2, 'b': 10, 'f': lambda x,y: x**y})

help(eval)                          # eval(src[, globals[, locals]]) -> value

from math import pi,cos,sin,tan,atan
bindings['p'] = pi
# eval('a + sin(p/2)', bindings)    # 'sin' not defined
globals()['sin']
eval('a + sin(p/2)', globals(), bindings)


# Evaluating formulae "Matlab style"
class StringFunction:
    def __init__(self, expression):
        self._expr = expression

    def __call__(self, x):
        return eval(self._expr)     # evaluate function expression!

f = StringFunction('1+sin(2*x)')
f._expr
f(pi/4)                             # same as StringFunction.__call__(f,pi/4)

# This makes it easy to build an interpreter! In fact, in most interpreted
# and hybrid programming languages (such as Lisp/Scheme, Python, ...), the
# interpreter is basically an "eval loop"!
# One could also write a Python app or game that is "moddable" i.e., that
# lets the user modify its behavior by injecting Python code dynamically.


# Executing code dynamically - 'eval' works for single expressions, 'exec'
# is for evaluating any Python code or even an entire script.
exec('c = 1 ; print(c)')
#eval('c = 1 ; print(c)')           # SyntaxError (two expressions)

# Another difference is that a call to 'exec' returns None while 'eval'
# returns the value of the expression that is evaluated.
print(eval('2 + 2'))
print(exec('2 + 2'))

bindings = {'a': 1, 'b': 2}         # dictionary of bindings -> scope
exec('c = a + b', bindings)
print(c)                            # original 'c' in main is unmodified
bindings['c']                       # 'c' in 'exec' scope i.e. bindings dic

help(exec)                          # exec(object[, globals[, locals]])

exec('four = 2 + 2')                # default 'exec' scope is main
print(four)

exec("""
def greet(s):
    print('hello, ' + s)
""")
greet('everyone')

# Finally, 'exec' can execute compiled code as well (see next section).


# WARNING: Never use 'eval' or 'exec' on some unknown function arguments or
# some imported code without checking thoroughly what it does! Because it
# could be a Python expression with unwanted or harmful side effects!
# For example, someone could pass __import__('os').system('rm -rf $HOME')
# which would totally erase your home directory!!!



################################
##
##  COMPILING PYTHON CODE
##

# Hybrid programming languages are faster than pure interpreted languages
# because they can compile the source code into some intermediate bytecode
# which is then translated in real-time to machine code... In Python we
# can explicity COMPILE a function into bytecode!

class StringFunction_compiled:      # faster with a compiled expression!
    def __init__(self, expression):
        self._compiled_expr = compile(expression, '<string>', 'eval')

    def __call__(self, x):
        return eval(self._compiled_expr)

import time

# Comparing performance: interpreted vs. compiled code
def timefc(expression, arg=pi/4, num=10000):

    func = StringFunction(expression)
    si = time.time()
    for x in range(num): func(arg)
    ei = time.time()
    
    func = StringFunction_compiled(expression)
    sc = time.time()
    for x in range(num): func(arg)
    ec = time.time()
    
    print(" interpreted time =", ei-si)
    print("    compiled time =", ec-sc)
    print("performance ratio =", round((ei-si)/(ec-sc),2))

timefc('atan(tan(atan(tan(atan(tan(atan(tan(x))))))))')
# e.g. ->
#  interpreted time = 0.21879982948303223
#     compiled time = 0.015627384185791016
# performance ratio = 14.0 !

# So we can do numerical calculations in Python with the performance of C!
# e.g., numpy module: all its functions are compiled, not interpreted.


# note: 'exec' actually compiles the Python code passed as argument (string)
# before executing it. 'eval' does not. One can also compile and save the
# code beforehand, then 'exec' will execute the bytecode directly.

# Compiling then executing code
ccode = compile('res = 11 + 22', '<string>', 'exec')

exec(ccode)
print(res)


# Comparing performance
#
# > python -mtimeit -s 'code = "a,b = 1,2 ; c = a * b"' 'exec code'
# 10000 loops, best of 3: 20.9 usec per loop
# vs. 
# > python -mtimeit -s 'code = compile("a,b = 1,2; c = a * b", \
#                                     "<string>", "exec")' 'exec code'
# 1000000 loops, best of 3: 0.637 usec per loop
# i.e., about 32 times faster for a very simple piece of code!
# (The more complex the code, the larger the performance gap.)


def timefact():
    def fact(n, f=1):
        if n == 1: return f
        else: return fact(n-1, n*f)
    code = 'print(fact(888))'
    bytecode = compile(code, '<string>', 'exec')

    se = time.time()
    eval(code)
    ee = time.time()
    
    sx = time.time()
    exec(code)
    ex = time.time()
    
    sc = time.time()
    exec(bytecode)
    ec = time.time()
    
    print("     eval code - time =", ee-se)
    print("     exec code - time =", ex-sx)
    print(" exec bytecode - time =", ec-sc)
    #print("performance ratio =", round((ee-se)/(ex-sx),2))
    #print("performance ratio =", round((ex-sx)/(ec-sc),2))
# e.g. ->
#     eval code - time = 0.0781095027923584
#     exec code - time = 0.0468752384185791
# exec bytecode - time = 0.03125262260437012

# note: All Python code imported from a module is automatically compiled the
# first time (or if the module file has changed) to a .pyc file. Code in the
# main is not compiled, unless explicitly as illustrated above.



################################
##
##  AUTOMATED CODE TESTING
##


# Assertions - check that some constraint is satisfied
assert 2+2 is 4

codeWorks = False 
#assert codeWorks, "this is not supposed to happen!"


# Testing specifications, using the doc string!
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":          # top-level script
    import doctest
    doctest.testmod()

    
def nF(n):
    """Trick function that achieves nF(nF( n )) == -n

    Testing:
    >>> for n in range(-10, 10): assert nF(nF(n)) == -n

    Alternative solution: return n * 1j
    """
    if n > 0:
        if n % 2 == 0: return n - 1
        else: return -n - 1
    elif n < 0:
        if n % 2 == 0: return n + 1
        else: return -n + 1
    else: return 0
        


##
##  END
##
