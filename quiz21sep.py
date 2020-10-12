# pop quiz Sept 21, 2020

# Step 0: Add your name and pledge

# Step 1: Run this file in IDLE so you know it got downloaded ok.
#         It should print True four times.

# Step 2: Implement this function so it works correctly, using recursion, and
#         not using the built-in 'in' function.

def member(x,L):
    '''Assume L is a list. Return True or False according to whether x is in L.'''
    exists = False
    
    if L == []:
        return exists
    
    if L[0] == x:
        exists = True
        return exists
    
    else:
        member(x,L[1:])
 


def test():
    '''Prints True for each successful test'''
    print( member(42, [42, 20, 100]) == True )        
    print( member(42, [12,17,5,8,42]) == True )
    print( member(42, [12,17,5]) == False )
    print( member(42, []) == False )

test()  

