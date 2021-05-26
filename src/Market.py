import numpy as np
from src.OrderBook import OrderBook
from src.Order import Order

class Market:

    def __init__(self, agents : dict):
        # order list. Initialize it into a bull market to help the traders :)
        self.orderData = list(range(0,15))
        self.orderBook = OrderBook(market=self)
        self.agents = agents
        self.addMarketToAgents()

    # Get the last seconds seconds of the order data
    def getMarketData(self, ticks: int):
        if ticks > len(self.orderData):
            return self.orderData
        else:
            return self.orderData[-ticks:]

    def getCurrentPrice(self):
        return self.orderBook.lastExecutedPrice

    def placeOrder(self, order: Order):
        self.orderBook.matchOrder(order)

    def backFillPriceHistory(self):
        pass

    def settleOrder(self, order: Order):
        settlee = self.agents[order.agentId]
        settlee.buyingPower += order.amountChanged
        settlee.shares += order.sharesChanged
        order.amountChanged = 0
        order.sharesChanged = 0

        # only limit orders have a price
        if order.price and order.shares == 0:
            if order in self.orderBook.pricePoints[order.price]:
                del self.orderBook.pricePoints[order.price][self.orderBook.pricePoints[order.price].index(order)]
    
    def addMarketToAgents(self):
        for k,v in self.agents.items():
            v.market = self

    def printAgentsHoldings(self):
        for k,v in self.agents.items():
            print(v.buyingPower, v.shares)

   