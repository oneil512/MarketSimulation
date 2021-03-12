import numpy as np

class Market:

    def __init__(self, agents : dict):
        self.orderData = np.array()
        self.orderBook = OrderBook()
        self.agents = agents

    # Get the last seconds seconds of the order data
    def getMarketData(seconds: int):
        return this.orderData[-seconds:]

    def placeOrder(order: Order):
        self.orderBook.insertOrder(order)

    def backFillPriceHistory():
        pass

    def settleOrder(order: Order):
        settlee = self.agents[order.id]
        settlee.buyingPower += order.amountPaid
        settlee.shares += order.sharesBought
