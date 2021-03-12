import numpy as np

class OrderBook:

    #array of price points with list of buy sell orders at each price point
    def __init__(self, market : Market):
        # 100 increments per dollar
        # 1000 dollar range on the order book
        self.dollarIncrements = 100
        self.orderBookDepth = 1000
        keys = list(range(0, self.orderBookDepth * self.dollarIncrements, 1))
        self.pricePoints = {key / self.dollarIncrements: None for key in keys}
        self.lastExecutedPrice = 0.00
        self.market = market

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
        price = self.lastExecutedPrice
        while not orderFilled and not price < 0 and not price > self.orderBookDepth:
            orderList = self.OrderBook[price]
            if buy:
                for o in orderList:
                    if buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares -= order.shares

                            o.sharesChanged -= order.shares
                            o.amountChanged += order.shares * price

                            order.sharesChanged += order.shares
                            order.amountChanged -= order.shares * price

                            order.shares = 0
                            orderFilled = True
                            order.filled = True
                            self.lastExecutedPrice = price
                            break
                        else:
                            order.shares -= o.shares
                            o.sharesChanged -= o.shares
                            o.amountChanged += o.shares * price

                            order.sharesChanged += o.shares
                            order.amountChanged -= o.shares * price

                            o.shares = 0
                            o.filled = True

                            self.lastExecutedPrice = price
                price += 1 / self.dollarIncrements
                
            else:
                for o in orderList:
                    if buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares += order.shares

                            o.sharesChanged += order.shares
                            o.amountChanged -= order.shares * price

                            order.sharesChanged -= order.shares
                            order.amountChanged += order.shares * price

                            order.shares = 0
                            orderFilled = True
                            order.filled = True
                            self.lastExecutedPrice = price
                            break
                        else:
                            order.shares -= o.shares
                            o.sharesChanged += o.shares
                            o.amountChanged -= o.shares * price

                            order.sharesChanged -= o.shares
                            order.amountChanged += o.shares * price

                            o.shares = 0
                            o.filled = True
                            
                            self.lastExecutedPrice = price
                price -= 1 / self.dollarIncrements

        if not orderFilled:
            print('Market ran out of liquidity!')

        self.market.settleOrder(order)
        

    def matchLimitOrder(buy : bool):
        pass

