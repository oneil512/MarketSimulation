import numpy as np

class Market:

    def __init__(self):
        self.orderData = np.array()
        self.orderBook = OrderBook()

    # Get the last seconds seconds of the order data
    def getMarketData(seconds: int):
        return this.orderData[-seconds:]

    def placeOrder(order: Order):
        self.orderBook.insertOrder(order)

    def backFillPriceHistory():
        pass
