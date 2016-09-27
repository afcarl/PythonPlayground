"""
Apply recursion to solve a problem, practice formulating and analyzing algorithms.
 In the US, coins are minted with denominations of 50, 25, 10, 5, and 1 cent. 
 An algorithm for making change using the smallest possible number of coins repeatedly 
 returns the biggest coin smaller than the amount to be changed until it is zero. 
 For example, 17 cents will result in the series 10 cents, 5 cents, 1 cent, and 1 cent. 
"""

denominations = [50, 25, 10, 5, 1]


def make_change(amount):
    if amount < 0:
        print 'Amount cannot be negative'
        return 0
    if amount == 0:
        return amount
    index = 0
    while amount < denominations[index]:
        index += 1
    print denominations[index],
    make_change(amount - denominations[index])
    return 0


make_change(-1)
make_change(17)
