import unittest

from src.Market import Market
from src.Agent import Agent
from src.Order import Order
from src.AgentFactory import AgentFactory


class TestOrders(unittest.TestCase):
    def setUp(self) -> None:
        self.mmShares = 1000000
        self.mmMoney = 1000000

        self.buyerShares = 0
        self.buyerMoney = 10000

        self.sellerShares = 1000
        self.sellerMoney = 0

        self.marketMaker = Agent(riskPropensity=.1, buyingPower=self.mmMoney, shares=self.mmShares)
        self.buyer = Agent(riskPropensity=.1, buyingPower=self.buyerMoney, shares=self.buyerShares)
        self.seller = Agent(riskPropensity=.1, buyingPower=self.sellerMoney, shares=self.sellerShares)
        self.market = Market({self.buyer.id: self.buyer, self.seller.id: self.seller, self.marketMaker.id: self.marketMaker})

    def testMarketBuy(self):
        sharesToBuy = 20
        price = 10.0
        self.marketMaker.placeOrder(orderType=1, buy=False, shares=1000, price=price)
        self.buyer.placeOrder(0, True, sharesToBuy)

        self.assertTrue(self.buyer.shares == sharesToBuy)
        self.assertTrue(self.marketMaker.shares == (self.mmShares - sharesToBuy))
        self.assertTrue(self.buyer.buyingPower == self.buyerMoney - sharesToBuy * price)



if __name__ == '__main__':
    unittest.main()


