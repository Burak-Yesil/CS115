

from cs115 import map, reduce


def add(x,y):
    ''' Returns the sum of two numeric inputs'''

    return x + y

def mult(x,y):
    '''Returns the product of x and y'''

    return x * y

def factorial(n):
    ''' Takes a positive integer n and returns its factorial'''
    if n==0:
        return 1;
    else:
        return n * factorial(n-1)

def mean(L):
    ''' Takes in a list and returns the average of the whole list'''

    sum = reduce(add, L)
    average = sum/len(L)

    return average
def returnElement(n):
    return n;
    
def prime(n):
    ''' takes input n and returns whether the integer inputed is a prime number'''
    f = divides(n)
    map(f,range(2,n))


def divides(n):
    def div(k):
        return n % k == 0
    return div
