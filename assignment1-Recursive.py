# author: Ashish Tamrakar
# Advanced Database Systems
# Date: 2016/01/27
# Python ver 2.7.10
# Finding the minimum number of coins for the money using recursive approach

INFINITY = 99999
def RecursiveChange(money, coins):
    """
    Returns the minimum number of coins and change of money from the given coins and money.
    :param money: Money to be changed.
    :param coins: Coins that can be used to change the money.
    :return: minCoins and change
    """
    change = []
    if (money == 0):
        return {'minCoins': 0, 'change': change}
    minCoins = INFINITY
    for changeValue in coins:
        if (money >= changeValue):
            list = RecursiveChange(money - changeValue, coins)
            numcoins = list['minCoins']
            if ((numcoins + 1) < minCoins):
                change = list['change']
                minCoins = numcoins + 1
                change.append(changeValue)
    return {'minCoins': minCoins, 'change': change}


# To check the minimum number of coins required for the money in recursive way.
def main():
    """
    Main Function to call the RecursiveChange()
    :return: None
    """
    # coins = [6,5,1]
    # money = 20
    coins = [50, 25, 20, 10, 5, 1]
    money = 40
    print "Coins:", coins
    print "Money to be changed:", money
    listChange = RecursiveChange(money, coins)
    print "Minimum number of Coins:", listChange['minCoins']
    print "Change:", listChange['change']

# To check the time of the execution of the main function
import timeit
timer = timeit.Timer(stmt='main()', setup='from __main__ import main')
print timer.timeit(1)
