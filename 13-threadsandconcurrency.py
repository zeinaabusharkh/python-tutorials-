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
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency: simple threads, subclassing, timer threads,
##                          more examples, coroutines, asynchronous generators
##  14. Miscellanies and References
##



###############################################################################
###
###   13. THREADS AND CONCURRENCY
###



################################
##
##  SIMPLE THREADS
##


from threading import Thread
from time import sleep
from random import randint

# Threads in Python are very similar to that in Java. This example creates
# a number of threads, sets simpleTask() as their target/run method/function,
# then start each, which initializes the thread and calls its run method
def ten_little_threads(number = 10):

    def simple_task(thread_id, waiting_time):
        # do something ...
        print(" thread {} sleeping ({}) ".format(thread_id, waiting_time))
        sleep(waiting_time)
        print(" thread {} awaking ".format(thread_id))
    
    for num in range(number):
        print(" thread {} starting ".format(num))
        t = Thread(target=simple_task,        # "run" function (thread body)
                   args=(num, randint(1,10))) # and its parameters 
        t.start()

#ten_little_threads()


# Thread subclass
class simple_thread(Thread):

    def __init__(self, target=None, args=()):
        Thread.__init__(self, target=target)
        self.args = args
        return
    
    def run(self):
        # do something ...
        print(" thread {} sleeping ".format(self.args[0]))
        sleep(self.args[1])
        print(" thread {} awaking ".format(self.args[0]))
        return

def more_little_threads(number = 10):
    for num in range(number):
        print(" thread {} starting ".format(num))
        t = simple_thread(args=(num, randint(1,10)))
        t.start()

#more_little_threads()



################################
##
##  TIMER THREADS
##


from threading import Timer

def delayed_task(task_name):
    print('task', task_name, 'working')
    return

def little_timers(sleep_time=4):
    t1 = Timer(2, delayed_task, args=('t1',))
    t2 = Timer(6, delayed_task, args=('t2',))
    print('starting timers')
    t1.start()
    t2.start()
    sleep(sleep_time)           # wait before cancelling task #2
    t2.cancel()                 # if sleep_time > 6, task #2 will never run

#little_timers()



# to be expanded ...

# See also: https://jeffknupp.com/blog/2012/03/31/pythons-hardest-problem/



################################
##
##  COROUTINES
##


# There are three big problems with threads [http://www.effectivepython.com]
# (1) They require special tools to coordinate with each other safely. This
# makes code that uses threads harder to reason about than procedural, single-
# threaded code. This complexity makes threaded code more difficult to extend
# and maintain over time.
# (2) Threads require a lot of memory, about 8MB per executing thread. On many
# computers that amount of memory doesn't matter for a dozen threads or so.
# But what if you want your program to run tens of thousands of functions
# "simultaneously"? It won't work.
# (3) Threads are costly to start. If you want to constantly be creating new
# concurrent functions and finishing them, the overhead of using threads
# becomes large and slows everything down.

# Python can work around all these issues with coroutines. Coroutines let you
# have many seemingly simultaneous functions in your Python programs. They are
# implemented as an extension to generators. The cost of starting a generator
# coroutine is a function call. Once active, they each use less than 1KB of
# memory until they're exhausted.

# Coroutines work by enabling the code consuming a generator to 'send' a value
# back to the generator function after each 'yield' expression. The generator
# function receives the value passed to the 'send' function as the result of
# the corresponding 'yield' expression...
# (See also section 08. Iterators/Generators.)

# Example: A generator coroutine that yields the minimum value it has been
# sent so far. Here the bare 'yield' prepares the coroutine with the initial
# minimum value sent in from the outside. Then the generator repeatedly yields
# the new minimum in exchange for the next value to consider.

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

# The code consuming the generator can run one step at a time and will output
# the minimum value seen after each input.

it = minimize()
next(it)            			# prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

# The generator function will seemingly run forever, making forward progress
# with each new call to 'send'. Like threads, coroutines are independent
# functions that consume inputs from their environment and produce resulting
# outputs. The difference is that coroutines pause at each 'yield' expression
# in the generator function and resume after each call to 'send' from the
# outside.

# This behavior allows the code consuming the generator to take action after
# each yield expression in the coroutine. The consuming code can use the
# generator's output values to call other functions and update data structures.
# Most importantly, it can advance other generator functions until their next
# yield expressions. By advancing many separate generators in lockstep, they
# will all seem to be running simultaneously, mimicking the concurrent
# behavior of Python threads.


# See about streams and coroutines, and a produced-filter-consumer example at
# http://wla.berkeley.edu/~cs61a/fa11/lectures/streams.html and
# https://jeffknupp.com/blog/2013/04/07/
#     improve-your-python-yield-and-generators-explained/

import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)

def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0
    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

def producer_consumer_demo():
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)
    for _ in range(10):
        print('Producing...')
        next(producer)

#producer_consumer_demo()



################################
##
##  ASYNCHRONOUS GENERATORS [v3.6]
##


# Example - see https://www.python.org/dev/peps/pep-0525/
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def run():
    async for i in ticker(1, 10):
        print(i)

import asyncio
def async_ticker_demo():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()

#async_ticker_demo()



################################
##
##  ASYNCHRONOUS COMPREHENSIONS [v3.6]
##


# Using async for in list/set/dict comprehensions and generator expressions:
#
# result = [i async for i in aiter() if i % 2]
#
# In addition, await expressions are supported in all kinds of comprehensions:
#
# result = [await fun() for fun in funcs if await condition()]

# See https://www.python.org/dev/peps/pep-0530



##
##  END
##
