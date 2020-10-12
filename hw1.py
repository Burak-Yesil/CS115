# Burak Yesil
# "I pledge my honor that I have abided by the Stevens honor system".

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

    
def prime(n):
    ''' takes input n and returns whether the integer inputed is a prime number'''
    lst = map(divides(n),range(2,n))
    return (False) if(True in lst) else (True)



def divides(n):
    '''The divides function takes in an integer n and checks whether or not when n
    is divided by another integer input k the remainder is 0. If the remainder is
    0 the fucntion returns true. '''
    
    def div(k):
        return n % k == 0
    return div


def Test_All():
    '''Tests all test cases below'''
    Test_Factorial_Function()
    Test_Mean_Function()
    Test_Prime_Function()

def Test_Factorial_Function():
    '''Tests to see if the Factorial Function Is working.'''
    print("Test Results of Factorial Function:")
    print( "Does 7 factorial equal 5040? ", factorial(7) == 5040)
    print( "Does 10 factorial equal 3628800? ", factorial(10) == 3628800)
    print( "Does 12 factorial equal 479001600? ", factorial(12) == 479001600)
    print( "Does 5 factorial equal 120? ", factorial(5) == 120)
    print()
 
def Test_Mean_Function():
    '''Tests to see if the Mean Function Is working.'''
    print("Test Results of Mean Function:")
    print( "Does the mean of [1, 2, 3]  equal 2? ", mean([1, 2, 3]) == 2)
    print( "Does the mean of [1,2,3,4,5]  equal 3? ", mean([1,2,3,4,5]) == 3)
    print( "Does the mean of [2,2]  equal 2? ", mean([2,2]) == 2)
    print( "Does the mean of [1, 1, 1] equal 1? ", mean([1, 1, 1]) == 1)
    print()

def Test_Prime_Function():
    '''Tests to see if the Prime Function Is working.'''
    print("Test Results of Prime Function:")
    print( "Is 7 a prime number? ", prime(7))
    print( "Is 102 a prime number? ", prime(102))
    print( "Is 24 a prime number?", prime(24))
    print( "Is 101 a prime number?", prime(101))
    print()

