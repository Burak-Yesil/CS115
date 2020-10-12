#Burak Yesil
# "I pledge my honor that I have abided by the Steven's honor code."


def getValueOfListItems(itemList):
    '''Returns the total value of all the items in the itemlist.'''
    print(itemList)
    if itemList == []:
        return 0
    else:
        return itemList[0][0] + getValueOfListItems(itemList[1:])
    
    
#print(getValueOfListItem([[2, 100], [3, 112], [4, 125]]))

def myMax(X,Y):
    '''Given two input lists. myMax returns the list with the highest
    value'''
    print(X)
    print(Y)
    if getValueOfListItems(X) > getValueOfListItems(Y):
        return X
    elif getValueOfListItems(X) == getValueOfListItems(Y):
        return X
    else:
        return Y
    


def helper(capacity, itemList):
    '''The helper function goes through every possible list combination and
    figures out the max value list.'''
    L = itemList
    
    if capacity <= 0:
        return [0,[0]]
    elif L == []:
        return [0,[]]
    else:
        print(L)
        useit = L[0] + helper(capacity-L[0][0], L[1:])
        loseit = helper(capacity, L[1:])

        return myMax(useit,loseit)



def knapsack(capacity, itemList):
    ''' Uses helper function and getValueOfListItems function to print out
    the maximum value of the list and the list itself with the info of each
    item.'''
    
    #L = helper(capacity,itemList)
    #return (getValueOfListItems(L),L)
    if capacity == 0 or itemList == []:
        return [0,[]]
    if itemList[0][0] > capacity:
        return knapsack(capacity,itemList[1:])
    else:
        use = knapsack(capacity-itemList[0][0],itemList[1:])
        lose = knapsack(capacity,itemList[1:])

        print(use)
        print(lose)
    if lose[0] > use[0] + itemList[0][0]  :
            return lose
    else:
            return [itemList[0][0] + use[0],[]+use[1]] 
            
    
def knapsack(M, L):

    def getValue(L):
        if L == []:
            return 0
        else:
            if isinstance(L[0], list) != True:
                L = [L]
            return L[0][1] + getValue(L[1:])
    def generateList(M, L, a):
        if M == 0:
            return []
        elif L == []:
            return []
        elif M - L[0][0] >= 0:
            use = [L[0]] + generateList(M-L[0][0],L[1:],a+1)
            lose = generateList(M,L[1:],a+1)
            if getValue(use) >= getValue(lose):
                return use
            else:
                return lose
        else:
            return generateList(M,L[1:],a+1)
    return [getValue(generateList(M,L,0)), generateList(M,L,0)]

