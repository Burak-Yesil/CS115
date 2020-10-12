'''
Created on _______09-19-2020________________
@author:   _______Burak Yesil________________
Pledge:    _______"I pledge my honor that I have abided by the stevens honor system"________________

CS115 - Hw 2
'''
import sys
from dict import *
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores =  [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


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


def explode(s):
    '''list of characters in string s'''
    
    if s=="":
        return []
    else:
        return [s[0]] + explode(s[1:])



def findElementAndRemoveElement(L, element):
    '''Finds an element in a list and removes the element from the list '''
    if L == []:
        return []
    elif L[0] == element:
        return L[1:]
    else:
        return [L[0]] + findElementAndRemoveElement(L[1:],element)
 
    

    
def scoreList(Rack):
    '''Takes an input rack which is a list of lowercase letters and returns every word
    in the dictionary that can be made with the letters in rack. '''
    
    def pairReturner(word):
        #returns word and word score in a list
        return [word,wordScore(word, scrabbleScores)]

    def isPairValid (pair):
        #checks if pair is valid 
        w = pair[0]
        cRack = []
        cRack.extend(Rack)
        def removeLetter(s,l):
            #removes letter from list
            if s == "":
                return True
            elif s[0] in l:
                l = findElementAndRemoveElement(l,s[0])
                return removeLetter(s[1:],l)
            else: return False
        
        return removeLetter(w,cRack)
    
    return list(filter(isPairValid, map(pairReturner, Dictionary)))

     


def bestWord(Rack):
    '''Takes input Rack and returns the word with the highest score along with its score. '''
    def getBetterPair(x, y):

        if x[1]>y[1]: return x
        else: return y

    return reduce(getBetterPair, scoreList(Rack))



