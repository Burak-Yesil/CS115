'''
Created on _09-27-2020______________________
@author:   _Burak Yesil______________________
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import map
' PROBLEM 0'
' Implement the function giveChange() here:'
def minList(x,y):
    '''Returns the short list of the two inputed lists '''
            
    if len(x)<=len(y):
        return x
    else:
        return y

def helper(amount,coins):
    '''This helper function returns the shortest list of coins that add to the total amount.'''
    if len(coins) > 1:
        if amount <= 0:
            return []
        elif amount == 1:
            return [1]
        elif amount < coins[len(coins)-1]:
            return helper(amount,coins[:len(coins)-1])
        else:
            useit = [coins[len(coins)-1]] + helper(amount-coins[len(coins)-1], coins)
            loseit = helper(amount, coins[:len(coins)-1])
            return minList(useit,loseit)
    else:
        if amount == 0:
            return []
        else:
            useit = [coins[len(coins)-1]] + helper(amount-coins[len(coins)-1], coins)
            return useit
    
        
def giveChange(amount, coins):

    return [len(helper(amount,coins)), helper(amount,coins)]



# your code goes here

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def letterScore(letter, scorelist):
    ''' The function accepts a lowercase letter and a scorelist as its two inputs.
    The function returns the score acosiated with the lower case letter after refering to the
    scorelist.'''
    
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    ''' The function gets a string input S and returns the total score of each characters added up.  '''
    if S == "":
        return 0
    else:
        return (letterScore(S[0],scorelist)) + wordScore(S[1:],scorelist)
    
def addLists(x,y):
    if x == []:
        return []
    else:
        element = [x[0],y[0]]
        return element + addlists(x[1:],y[1:])
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    ''
    return None  # your code goes here'''

    def helper(word):
        return [word,wordScore(word,scores)]
    
    return map(helper,dct)
            
        


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''

    if n == 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):

    if n == 0:
        return L
    else:
        return drop(n-1,L[1:])
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
        

