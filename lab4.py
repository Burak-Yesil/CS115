#Burak Yesil
# "I pledge my honor that I have abided by the Steven's honor code."


def getValueOfListItems(itemList):
    '''Returns the total value of all the items in the itemlist.'''
    if itemList == []:
        return 0
    else:
        if isinstance(itemList[0], list) != True:
            itemList = [itemList]
        return itemList[0][1] + getValueOfListItems(itemList[1:])
    
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
    if capacity == 0:
        return []
    elif itemList == []:
        return []
    elif capacity - itemList[0][0] >= 0:
        use = [itemList[0]] + helper(capacity-itemList[0][0],itemList[1:])
        lose = helper(capacity,itemList[1:])
        if getValueOfListItems(use) >= getValueOfListItems(lose):
            return use
        else:
            return lose
    else:
        return helper(capacity,itemList[1:])



def knapsack(capacity, itemList):
    ''' Uses helper function and getValueOfListItems function to print out
    the maximum value of the list and the list itself with the info of each
    item.'''
    return [getValueOfListItems(helper(capacity,itemList)), helper(capacity,itemList)]
    




