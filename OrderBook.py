import numpy as np

class OrderBook:

    #array of price points with list of buy sell orders at each price point
    def __init__(self):
        # 100 increments per dollar
        # 1000 dollar range on the order book
        self.dollarIncrements = 100
        self.orderBookDepth = 1000
        keys = list(range(0, self.orderBookDepth * self.dollarIncrements, 1))
        self.pricePoints = {key / self.dollarIncrements: None for key in keys}
        self.lastExecutedPrice = 0.00

    def placeOrder(order: Order):
        if order.price > self.orderBookDepth or order.price < 0:
            print("invalid order placed: price not in range: ", price)
            return
        remainingOrder = self.matchOrder(order)
        self.pricePoints[order.price * 100].append(order)

    def matchOrder(order: Order):
        # Market order
        if order.orderType == 0:
            self.matchMarketOrder(order.buy)
        else:
            self.matchLimitOrder(order.buy)



    def matchMarketOrder(buy : bool):
        orderFilled = False
        check = self.lastExecutedPrice
        while not orderFilled:
            orderList = self.OrderBook[check]
            for o in orderList:
                if not o.buy:
                    if o.shares >= order.shares:
                        o.shares -= order.shares
                        order.shares = 0
                        orderFilled = True
                        order.filled = True
                        self.lastExecutedPrice = check
                        break
                    else:
                        order.shares -= o.shares
                        o.shares = 0
                        o.filled = True
                        self.lastExecutedPrice = check
            # Checked all orders at this price and still not filled
            if buy:
                check += 1 / self.dollarIncrements
            else:
                check -= 1 / self.dollarIncrements

    def matchLimitOrder(buy : bool):
        pass