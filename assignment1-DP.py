# author: Ashish Tamrakar
# Advanced Database Systems
# Date: 2016/01/27
# Python ver 2.7.10
# Finding the minimum number of coins for the money using dynamic programming approach.

INFINITY = 99999


def DPchange(money, coins):
    """
    Returns the minimum number of coins and denominations change of the minimum number of coins.
    :param money: Money to be changed.
    :param coins: Coins that are available.
    :return: minMoney and change
    """
    minNumCoins = [0]
    change = [0] * (money + 1)
    for m in range(1, money + 1):
        minNumCoins.append(INFINITY)
        for i in range(0, len(coins)):
            if (m >= coins[i]):
                if (minNumCoins[m - coins[i]] + 1 < minNumCoins[m]):
                    minNumCoins[m] = minNumCoins[m - coins[i]] + 1
                    change[m] = coins[i]
    return {'minMoney': minNumCoins[money], 'change': change}


def printCoins(coinsUsed, money):
    """
    Prints the denominations of the changes of the minimum number of Coins
    :param coinsUsed: Coins used for change of the minimum number of coins.
    :param money: Money to be changed.
    :return: None
    """
    allChangeItems = []
    while money > 0:
        coinUsed = coinsUsed[money]
        allChangeItems.append(coinUsed)
        money = money - coinUsed
    listChange = dict((i, allChangeItems.count(i)) for i in allChangeItems)
    for coin, nums in listChange.items():
        print nums, coin, "cents"


def main():
    """
    Main function to initialize and call the DPchange function and printCoins function.
    :return: None
    """
    # coins = [6, 5, 1]
    # money = 766
    coins = [50,25,20,10,5,1]
    money = 40
    print coins
    print money
    value = DPchange(money, coins)
    print "Minimum number of coins: ", value['minMoney']
    printCoins(value['change'], money)


# To check the time of the execution of the main function
import timeit

timer = timeit.Timer(stmt='main()', setup='from __main__ import main')
print timer.timeit(1)
