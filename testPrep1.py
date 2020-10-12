# CS 115A Fall 2020 - practice exercise for test

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the 
# IDLE to edit this file and check your solutions
# Zoom for the class meeting; use private chat to Dave or TAs if needed.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
#
# Hint: If some of your code doesn't work, comment it out and write a note.
# 
# Name and pledge:
#
#
#
#
#
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok, and have 
# cs115.py in the same folder.  There should be no error.
###########################################################################

from cs115 import *

###########################################################################
# STEP ONE:
# Using the definition of LCS below, show the trace of function calls
# for the expression LCS("hi", "bi").  Use indentation to show which 
# calls result from previous calls.
###########################################################################

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

"""
TODO PUT YOUR TRACE HERE INSIDE THIS COMMENT

LCS("hi", "bi")
    LCS("hi", "i")
        LCS("hi","")
            0
        LCS("i","i")
            1 + LCS("","")
                0

                #don't write return 0
                
    LCS("i", "bi")
        LCS("i","i")
            1 + LCS("","")
                0
        LCS("","i")
            0
"""

###########################################################################
# STEP TWO:
# Complete the definition of rev below, so that reverse_alt works correctly.
# Your code should be tail-recursive, using the parameter acc as accumulator.
###########################################################################


def reverse(L):
    '''reverse a list'''
    if L == []: return []
    else: return reverse(L[1:]) + [L[0]]

def reverse_alt(L):
    def rev(acc, L):
        '''.....define this using recursion on L,
        so we can use L==[], L[0], and rev(...,L[1:])'''

        pass # TO-DO your code goes here
    
    return rev([], L)

    # Hint: a trace of your code should look like this:
    #     reverse_alt([a,b,c,d])
    #       rev([], [a,b,c,d])
    #         rev([a], [b,c,d])
    #           rev([b,a],[c,d])
    #             rev([c,b,a],[d])
    #               rev([d,c,b,a],[])
                  

def testReverse():
    assert reverse(['hi','there']) == reverse_alt(['hi','there'])
    assert reverse(range(10)) == reverse_alt(range(10))
    assert reverse([]) == reverse_alt([])


