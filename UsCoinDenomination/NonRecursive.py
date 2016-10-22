"""
Give an O(1) (non-recursive!) algorithm to compute the number of returned coins.
"""

# denominations = [50, 25, 10, 5, 1]
denominations = [10,6,1]

def make_change(amount):
    if amount < 0:
        print 'Amount cannot be negative'
        return 0
    if amount == 0:
        return amount
    if amount in denominations:
        print amount
        return amount
    for coin in denominations:
        coins = amount / coin
        if coins > 0:
            print (str(coin) + ' ') * coins,
            amount -= coin * coins


make_change(-1)
#make_change(50)
#make_change(25)
make_change(18)
