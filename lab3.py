
#Burak Yesil
#" I pledge my honor that I have abided by the Stevens honor system".

def change(amount, coins):
    '''Returns the smallest amount of coins to get to amount'''

    if amount <= 0:
        return 0
    elif coins == []    :
        return float("inf")
    elif amount == 1:
        return 1
    elif amount < coins[0]:
        return change(amount,coins[1:])
    else:
        useit = 1 + change(amount-coins[0], coins)
        loseit =  change(amount, coins[1:])
        return loseit
    
