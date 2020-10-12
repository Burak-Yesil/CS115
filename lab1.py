
#Burak Yesil 
#"I pledge my honor that I have abided by the Stevens Honor System."


from cs115 import map, reduce
import math

def inverse(n):
    ''' returns the inverse of the input value as a floating point
    input value could be either an integer or floating point. '''
    return 1/n

def add(x,y):
    '''adds the two input values
    input values are could be either integers or floating point.'''
    
    return x+y

def e(n):
    ''' The e(n) function approximates the value of e using a taylor expandsion
    it takes an integer in as an input and returns the approximation of the value of e'''
    lst = map(math.factorial, range(1,n+1))
    lst2 = map(inverse,lst)
    total = reduce(add,lst2)
    return total + 1

def error(n):
    ''' The error(n) function returns the difference between the approximation and
    actual value of e. The function takes in a integer value n and plugs it in to the e(n)
    function to approximate the value of e.'''
    difference = math.e - e(n)
    difference = abs(difference)
    return differencespot
    
  
