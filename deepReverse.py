
def deepReverse(L):
    ''' This function the order of the elements in a list and returns the final list. If an element
    in the list is also a list that list is also reversed. '''
    
    if (isinstance(L[0],list)):
        return deepReverse(L[-1]) + deepReverse(L[1:])
    else:    
        if (L == []):
            return []
        else:
            return [L[-1]] + deepReverse(L[0:length(L)-1])
            
