###############################################################################
##
##  PYTHON SCRIPT DEMO -- Copyright Michel Pasquier, 2013-2018
##


## This Python script demo is part of section 01 (Introduction to Python).
## When executing a .py file (e.g. by double-clicking it) a Python shell is
## created that interprets the code, and quits - unless the user is prompted
## or a GUI is launched (that must be manually closed via a menu or button).


# People routinely run scripts from the Terminal in UNIX/Linux (and now also
# in macOS and Windows), to perform quickly all kind of tasks that would be
# tedious and time-consuming if done manually, but are easy to automate.

# The example below realizes a typical use case where one wishes to rename
# hundreds ot thousand of files, following a given pattern. Here it replaces
# space characters by hyphens; also changes all to lower case.


import os

""" 
Renames all files in the current directory to be "Unix friendly" i.e.
(1) Replaces all space characters by hyphens
(2) Changes to lowercase (not a Unix requirement, just looks better ;)
"""

path =  os.getcwd()                 # get current working directory
filenames = os.listdir(path)        # get list of files within

for name in filenames:              # rename all files
    os.rename(name, name.replace(" ", "-").lower())



##
##  END
##
