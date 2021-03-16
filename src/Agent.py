import numpy as np
from src.Market import Market
from src.Order import Order
import uuid


class Agent:
    # riskPropensity: float 0-1, 1 is highest risk
    # buyingPower: int 0-some number
    def __init__(self, riskPropensity: float, buyingPower:int, market:Market=None, shares=None):
        self.riskPropensity = riskPropensity
        self.buyingPower = buyingPower
        self.timePreference = self.getTimePreference()
        self.market = market
        self.id = uuid.uuid4()
        self.shares = 0 if shares is None else shares


    # Returns time preference in seconds
    # Range from 30 seconds to a month (2.6 million seconds)
    def getTimePreference(self) -> int:
        return (((self.riskPropensity - 0.0) * (2.6 * 10 ** 6 - 30)) / (1.0 - 0.0)) + 30

    def getTrendPreference(self) -> list:
        marketData = this.market.getMarketData(this.timePreference)
        return marketData

    def placeOrder(self, orderType:int, buy: bool, shares: int, price:float = None):
        order = Order(orderType=orderType, buy=buy, shares=shares, id_=self.id, price=price)
        self.market.placeOrder(order)

    # place well behaved trades!
    def policy():
        pass


