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
##  06. Exceptions and File I/O: exceptions, try/except block, exception class
##                               hierarchy, user-defined exceptions, file I/O
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
###   06. EXCEPTIONS AND FILE I/O
###
AssertionError


################################
##
##  EXCEPTIONS
##


# Syntax errors raise exceptions e.g.:
#4/0                                # ZeroDivisionError: division by zero
#int("no")                          # ValueError: invalid literal for int()
# forever loop: needs ctrl-C to stop, which raises a KeyboardInterrupt:
#while True: print('Hello world')

# Catching exceptions
def fte():
    while True:
        try:                        # get user input
            print(1 / int(input("Please enter a number: ")))
            break                   # exit while loop
        except ValueError:
            print("! Error: Not a number -- try again !")
        except ZeroDivisionError:
            print("! Error: Zero value -- try again !")
        except KeyboardInterrupt:   # ctrl-C disabled(!)
            print("! Oops... You can't even quit !")


# File input/output might raise exceptions
def ffe(file = "06-ExcAssertionErroreptionsAndFileIO.py"):
    try:
        f = open(file, 'r')
        # process content ...
    except IOError as err:
        print("I/O error: {0}".format(err))
    else:                           # always executed, if no interrupt
        print(file, 'has', len(f.readlines()), 'lines')
        f.close()

# ffe() vs. ffe('no_such_file')


import sys

def fff(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("error: division by zero")
    except KeyboardInterrupt:
        print("error: value needed")
    except:                         # catch-all (last) clause
        print("unknown error:", sys.exc_info()[0])
    else:
        print("the result is", result)
    finally:                        # always executed
        print("executing 'finally'")

# fff(8,2) vs. fff(8,0), fff(8,'two')



################################
##
## EXCEPTION CLASS HIERARCHY
##


# doc @ https://docs.python.org/3/library/exceptions.html
"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError = IOError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""



################################
##
## USER-DEFINED EXCEPTIONS
##


class CustomException(Exception):
    pass                            # (nothing to do)

def fme():
    print("program running")
    # some error occurs, hence:
    raise CustomException()         # or: raise(CustomException)

def fmex(n=0):
    def test(n):
        if n < 0: raise CustomException() # need catch in calling block

    print("program running")
    try:
        test(n)
        print("fine, n is", n)
        # ...
    except CustomException:
        print('! Custom exception occurred !')


class CustomExceptionWithValue(Exception):
    def __init__(self, value):
        self.value = value

CustomExceptionWithValue(4).value

def fmev(n=0):
    def test(n):
        if n < 0: raise CustomExceptionWithValue(n)

    print("program running")
    try:
        test(n)
        print("fine, n is", n)
        # ...
    except CustomExceptionWithValue as err:
        print('! Custom exception occurred ! value:', err.value)



################################
##
##  MORE FILE INPUT/OUTPUT
##


# Reading:
def procf(file = "4python-dev.txt"):
    try:
        f = open(file, 'r')         # type(f) is TextIOWrapper from io module
        for line in f:              # process file (code may vary) e.g.
            if line[0] == '*' and line[-2] == 'S':  # line[-1] is newline
                print(line)
    except IOError:
        print("Error: cannot open '{}'".format(file))
    else:
        f.close()                   # close file (always)

# 'with open as' auto-closing alternative
def procf2(file = "4python-dev.txt"):
    try:
        with open(file, 'r') as f:
            for line in f:
                if line[0] == '*' and line[-2] == 'S':
                    print(line)
    except IOError:
        print("Error: cannot open '{}'".format(file))

# lines = f.readlines()             # list of all lines, also: list(f)
# allcontent = f.read()             # whole file as a string

print(open('06-ExceptionsAndFileIO.py').read()) # prints this file

#exec(open('06-ExceptionsAndFileIO.py').read()) # much like import
# (guess why the above line must be commented out?!?)


# Writing:
# f = open(file, 'w')               # new file or overwrite
# f = open(file, 'a')               # append to existing file
# f.write("whatever you want ...")

# note: Python supports the standard JSON format for data exchange



# the following is included
# in case you uncomment
# the 'exec' line
# as defined
# above


'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!                                                                         !!!
!!!            If you keep seeing this again and again, it means            !!!
!!!                                                                         !!!
!!!                this file was "executed" programmatically.               !!!
!!!                                                                         !!!
!!!                    Type ctrl-C before it is too late.                   !!!
!!!                                                                         !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''


##
##  END
##

