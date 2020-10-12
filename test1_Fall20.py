# CS 115 Fall 2020 Test 1 

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the exam
# IDLE to edit this file and check your solutions
# Zoom for the class meeting - and you must stay in the meeting (muted) 
#   until you submit your test.  Use private chat to Dave or TAs if needed.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
# You have until 10:55am.
#
# Hint: If some of your code doesn't work, comment it out and write a note
# so your file still runs.
# 
# Name and pledge:
# Burak Yesil
#"I pledge my honor that I have abided by the Steven's honor code."
#
#
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok,
# and have cs115.py in the same folder.  There should be no error.
###########################################################################

from cs115 import *

print("So far so good...")

###########################################################################
# Question 1 (10 points) 
# Change the numbers in the list slices below, and nothing else, so that
# it prints   ['yes', 'we', 'survive', 'the', 'pandemic']
###########################################################################

L = ['yes', 'we', 'are', 'trying', 'to', 'survive', 'the', 'pandemic']

print(L[0:2]+L[5:])


###########################################################################
# Question 2 (10 points)
# Using the definition of LCS below, show the trace of function calls
# for the expression LCS('it', 'it').  Use indentation to show which 
# calls cause which.  Show all calls and nothing else.
###########################################################################

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

'''
TO-DO - your trace here

LCS('it','it')
    LCS('t','t')
        LCS('','')


'''


###########################################################################
# Question 3 (15 points) 
# Using the definition of fib below, show the trace of function calls
# for the expression fib(4). 
###########################################################################

def fib(n):
    if n==0 or n==1: 
        return n
    else: 
        return fib(n-1) + fib(n-2)

'''
TO-DO - your trace here

fib(4)
    fib(3)
        fib(2)
            fib(1)
            fib(0)
        fib(1)
    fib(2)
        fib(1)
        fib(0)

'''


###########################################################################
# Question 4 (10 points) 
# Implement the following, using map and lambda (not recursion).
# Hint: all it needs is a return statement.
# Hint: if you can't figure out lambda, just define a helper function.
###########################################################################

def addQ(strs):
    ''' Assume strs is a list of strings.
        Return a list of the same strings but with ? added at the end.'''
    
    return list(map(lambda x: x + "?", strs))


def testAddQ():
    assert addQ(["am", "I", "calm", "now"]) == ["am?", "I?", "calm?", "now?"] 


###########################################################################
# Question 5 (10 points) 
# Implement the following, using map and filter (not recursion).
###########################################################################

def withinRange(nums):
    '''Assume nums is a list of integers.  Return the sub-sequence of just
    ones in the range 0 to 10 inclusive.'''
    
    def inRangeOfTen(x):
        if (x in range(0,11)):
           return x
         
    
    newList = map(inRangeOfTen, nums)
    newList = filter(lambda x: x!=None,newList)
    
    return newList
   
def testWithinRange():
    assert withinRange([1, -2, 12, 5, 0, 10, 11]) == [1, 5, 0, 10]


###########################################################################
# Question 6 (15 points) 
# Implement the following, using recursion.
# Do not use filter or withinRange in your solution.
###########################################################################

def withinRangeRec(nums):
    '''Assume nums is a list of integers.  Return the sub-sequence of nums
    that are in the range 0 to 10 inclusive.'''
    def helper(acc,x):
        '''Checks whether or not each element of nums is in the range of 0 to 10 inclusive
        using tail recursion.'''
        
        if (x==[]):
            return acc
        else:
            if (x[0] in (range(0,11))):
                return helper(acc+[x[0]],x[1:])
            else:
                return helper(acc,x[1:])

    return helper([],nums)

def testWithinRangeRec():
    assert withinRangeRec([1, -2, 12, 5, 0, 10, 11]) == [1, 5, 0, 10]


###########################################################################
# Question 7 (15 points) 
# Implement the following, using recursion.
# Hint: If k is greater than zero, then n**k is n times what?  
###########################################################################

def exp(n,k):
    """exponent n**k, assuming k>=0 and n is a number"""
    if (k == 0): return 1
    elif(n == 0): return 0
    else:
        return n * exp(n,k-1)


###########################################################################
# Question 8 (15 points) 
# Replace each 'None' in this code, so it works correctly.
###########################################################################

def subsetB(target, L):
    '''Given a non-negative target capacity and list L of positive integers,
    determine whether some elements of L add up to exactly
    the target'''

    if target == 0:
        return True
    elif L == []:
        return False
    elif L[0] > target:
        return subsetB(target, L[1:]) # TO-DO
    else: 
        lose = subsetB(target, L[1:]) # TO-DO
        use =   subsetB(target-L[0], L[1:])
        return use or lose

def testSubsetB():
    assert subsetB(12, [2, 3, 4, 7, 10, 42])
    assert not subsetB(8, [2, 3, 4, 7, 10, 42]) 






