from cs115 import *
#Burak Yesil
#"I pledge my honor that I have abided by the stevens honor system".

def add(x,y):
    return x+y

def length(L):
    i = 0
    
    if(L == []):
        return 0
    else:
        i=i+1
        return i + length(L[1:])

def dot(L, K):
    ''' This function takes in two lists as inputs and returns
    the dot product of the two list inputs. '''
    
    if (length(L) != length(K)):
        return ("List lengths are not the same.")
    
    elif(L == []):
        return 0
    
    else:
        product = L[0]*K[0]
        return reduce(add,(product, dot(L[1:],K[1:])))

    

def explode(S):
    ''' This function takes in a string and returns a list that
    stores each individual character of the string input. '''
    if (S==""):
        return []
    else:
        lst = [S[0]]
        lst = lst + explode(S[1:])
        return lst



def ind(e,L):
    ''' This function takes in an element e and a squence L, which
    can be a string or a list, and returns the index of the first
    instance of the element e.  '''
    
    if(L == [] or L == ""):
        return 0
    elif(e == L[0]):
        return 1
    else:
        return 1 + ind(e,L[1:])
    

        

def removeAll(e,L):
    ''' This function takes in an element e and a squence L, which
    is a list, and returns a list which has each instance of the
    element e removed from it.  '''
     
    if(L == [] or L == ""):
        return []
    elif(e == L[0]):
        return [] + removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
        
        
        
def myFilter(f,L):
    ''' This function takes in two inputs a function f that returns true
    or false and a list L. The my filter function returns a list of the elements
    that the function f returned true for.'''

    if(L == [] or L == ""):
        return []
    elif(f(L[0])):
        return [L[0]] + myFilter(f,L[1:])
    else:
        return [] + myFilter(f,L[1:]) 
    

def deepReverse(L):
    ''' This function the order of the elements in a list and returns the final list. If an element
    in the list is also a list that list is also reversed. '''
    if L==[]:
        return []
    else:
        if(isinstance(L[0],list)):
            if (L==[]):
                return[]
            else:
                reversedList = [L[0][0]]
            L[0]=deepReverse(L[0][1:]) + reversedList
        secondReversedList = [L[0]]
    return deepReverse(L[1:]) + secondReversedList



