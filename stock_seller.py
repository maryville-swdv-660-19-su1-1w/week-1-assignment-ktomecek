###########################################################
# Written by Karl Tomecek 10/10/2018                      #
# Program Name: stock_seller.py                           #
# Week 7 Assignment                                       #
# Comments:                                               #
#                                                         #
###########################################################

import random
import math

#BEGIN CLASS
class StockHolding:
    def __init__( self, stockName, sharesPurchased, purchasePrice ):
        self.stockName = stockName.upper()
        self.sharesPurchased = sharesPurchased
        self.purchasePrice = purchasePrice
        self.currentPrice = purchasePrice
        #print("THIS IS JUST A PLACEHOLDER IN THE CONSTRUCTOR, REMOVE THIS MESSAGE!")
        
    def getSymbol(self):
        return self.stockName

    def getNumOfShares(self):
        return self.sharesPurchased
    
    def getPurchasePrice(self):
        return self.purchasePrice
    
    def getTotalCost(self):
        return self.sharesPurchased * self.currentPrice
    
    def estimateProfit(self, numSharesMaybeToSell):
        return numSharesMaybeToSell * (self.currentPrice - self.purchasePrice)
   
    def sellShares(self,numSharesToSell):
        try:
            if numSharesToSell > self.sharesPurchased or numSharesToSell < 0:
                raise ValueError
        except ValueError:
            print('VALUE ERROR: You cannot sell more shares then there are in the portfolio, or you entered an illegal value.')
        else:
            self.sharesPurchased = self.sharesPurchased - numSharesToSell
            
    def buyShares(self,numSharesToBuy):
        try:
            if numSharesToBuy < 0:
                raise ValueError
        except ValueError:
            print('VALUE ERROR: You entered an illegal value.')
        else:
            self.sharesPurchased = self.sharesPurchased + numSharesToBuy
            
    def setCurrentPrice(self):
        self.currentPrice = random.randint(1,30) * .5 #Simulate Stock price
#END CLASS    
        

def clearScreen():
    for i in range(15): #clear the screen
        print('\n')

def printMenu(testStock):
    print('Welcome to the stock broker system!  Shares Owned: {} - {} stock selling for ${:,.2f}'.format(testStock.sharesPurchased, testStock.stockName, testStock.currentPrice))
    print('****** MENU ******')
    print('buy    Purchase stocks')
    print('val    Get current value of stocks')
    print('est    Estimate the profit')
    print('sel    Sell stocks')
    print('quit   Quit the system\n')
    
def getUserSelection(testStock):
    notOK = True
    while notOK: # loop until valid input
        printMenu(testStock)
        userInput = input('Please enter your choice: ').lower().strip() # make lower so user can type in any case
        selectedIndex = ('buy val est sel quit').find(userInput) #returns -1 if not found
        if (selectedIndex == -1):
            print('\'{}\' is an invalid choice'.format(userInput))
        else:
            notOK = False
    return userInput

def main():
    clearScreen()
    goingRate = 2.50 # set an imaginary present stock price
    nameOfStock = input('Please enter the name of the stock you would like to purchase: ')
    testStockHolding = StockHolding(nameOfStock, 0, goingRate)
    clearScreen()
    choice = ''
    while (choice != 'quit'):
        choice = getUserSelection(testStockHolding)
        if choice == 'quit':
            print('Thank you for using the system.  Have a nice day!')
            break
        elif choice == 'val':
            testStockHolding.setCurrentPrice() #simulate real market by setting a random current price
            print ('\nPortfolio currently contains {} share(s) of {} with a value of ${:,.2f}.'.format(testStockHolding.getNumOfShares(), testStockHolding.getSymbol(), testStockHolding.getTotalCost()))
        elif choice == 'sel':
            numStocksToSell = int(input('Enter how many stocks to sell: '))
            testStockHolding.sellShares(numStocksToSell)
        elif choice == 'est':
            numStocksMaybeToSell = int(input('Enter how many stocks to sell: '))
            print('By selling {} stock(s) at ${}, the profit would be ${:,.2f}'.format(numStocksMaybeToSell, testStockHolding.currentPrice, testStockHolding.estimateProfit(numStocksMaybeToSell)))
        elif choice == 'buy':
            numStocksTobuy = int(input('Enter how many stocks to buy: '))
            testStockHolding.buyShares(numStocksTobuy)
        
main()

