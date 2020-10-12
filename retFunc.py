# Functions that return functions

from cs115 import *

# An example from hw1

def div(k):
    '''Checks whether 42 is evenly divisible by an integer k.'''
    return 42 % k == 0

def divides(n):
    '''Returns a function that checks whether a number divides n'''
    def div(k):
        return n % k == 0
    return div

def test_divides():
    f = divides(10)
    print("2 divides 10?", f(2) )
    print("3 divides 10?", f(3) )
    print("5 divides 15?", divides(15)(5) )

    
# Another example 

def increment(n):
    '''Returns a function that takes a number and adds it to n.'''
    def add_to(k):
        return k + n
    return add_to

def inc_all(nums, n):
    '''Add n to every number in a given list of numbers.'''
    return map(increment(n), nums)

def test_inc_all():
    '''Tests for inc_all. Correct tests print True.'''
    print(inc_all([], 2) == [])
    print(inc_all([1, 3, 5], 2) == [3, 5, 7])
    print(inc_all([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12])
