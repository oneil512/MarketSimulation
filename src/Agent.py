import numpy as np
from src.Market import Market
from src.Order import Order
import uuid
import random


class Agent:
    # riskPropensity: float 0-1, 1 is highest risk
    # buyingPower: int 0-some number
    def __init__(self, riskPropensity: float, buyingPower:int, market:Market=None, shares=None):
        self.riskPropensity = riskPropensity
        self.buyingPower = buyingPower
        self.initialBuyingPower = buyingPower
        self.timePreference = self.getTimePreference()
        self.market = market
        self.id = uuid.uuid4()
        self.shares = 0 if shares is None else shares


    # Returns time preference in seconds
    # Range from 30 seconds to a month (2.6 million seconds)
    def getTimePreference(self) -> int:
        return int((((self.riskPropensity - 0.0) * (1000 - 30)) / (1.0 - 0.0)) + 30)

    def getTrendPreference(self) -> list:
        marketData = self.market.getMarketData(self.timePreference)
        return marketData

    def placeOrder(self, orderType:int, buy: bool, shares: int, price:float = None):
        order = Order(orderType=orderType, buy=buy, shares=shares, id_=self.id, price=price)
        self.market.placeOrder(order)

    def limitBuy_(self):
        p = round(self.market.orderBook.lastExecutedPrice / 1.55 * random.random(), 2)
        if p <= 0:
            return

        shares = (.1 * self.buyingPower) // p
        self.placeOrder(orderType=1, buy=True, shares=shares, price=p)
        self.buyingPower -= shares * p


    def buy(self, percent=0.1):
            if self.buyingPower > 0:
                shares = (percent * self.buyingPower) // self.market.orderBook.lastExecutedPrice
                if shares > 0:
                    self.placeOrder(orderType=0, buy=True, shares=shares)

    def sell(self, percent=0.1):
        if self.shares > 0:
            shares = int(self.shares * percent) 
            self.placeOrder(orderType=0, buy=False, shares=shares)

    # place well behaved trades!
    def policy(self):
        

        data = self.market.getMarketData(self.timePreference)
        if data[0] < data[-1]:
            if self.shares * self.market.getCurrentPrice() + self.buyingPower > 1 + (self.riskPropensity * 10) * self.initialBuyingPower:
                #take profit
                self.sell(0.5)
                return
            self.buy()
        else:
            if random.random() < 0.5 * self.riskPropensity:
                self.buy(0.5)
            self.sell()

        if random.random() < .2:
            if self.buyingPower > (self.market.orderBook.lastExecutedPrice // 2):
                self.limitBuy_()
            


