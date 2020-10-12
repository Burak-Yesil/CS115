
'''
HW4
Burak Yesil
"I pledge my honor that I have abided by the Steven's honor system."
'''
from cs115 import *



def helper(L):
    '''Creates a new list by taking the sum of each adjacent number in
    the list with an additional element 1 at the end of each new list.  '''
    
    if L == []:
        return []
    elif len(L) == 1:
        return [L[0]] 
    else:
        return [L[0]+L[1]] + helper(L[1:]) 

    

def pascal_row(n):
    '''Returns the element in specified row of pascal triangle '''

    
    if n == 0:
        return [1]
    else:
        return [1] + helper(pascal_row(n-1))



def pascal_triangle(n):
    '''This function returns the pascal triangle up to the row
    n in the form of a list of inner lists. Each inner list represents
    each individual row.'''
    
    if n == 0:
        return [pascal_row(0)]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]
    

def test_pascal_row():
    '''Tests pascal_row function using assert statements. '''
    assert pascal_row(0)==[1]
    assert pascal_row(1)==[1, 1]
    assert pascal_row(5)==[1, 5, 10, 10, 5, 1]
    assert pascal_row(10)==[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    
def test_pascal_triangle():
    '''Tests pascal_triangle function using assert statments. '''
    assert pascal_triangle(0)==[[1]]
    
    assert pascal_triangle(1)==[[1], [1, 1]]
    
    assert pascal_triangle(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
    assert pascal_triangle(10)== [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                                  [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                                  [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1],
                                  [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
                                  [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

