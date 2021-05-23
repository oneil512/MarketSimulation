from __future__ import division
import numpy as np
from src import Market, Order
from decimal import *

class OrderBook:

    #array of price points with list of buy sell orders at each price point
    def __init__(self, market : Market):
        # 100 increments per dollar
        # 1000 dollar range on the order book
        self.dollarIncrements = 100
        self.orderBookDepth = 1000
        keys = list(range(0, self.orderBookDepth * self.dollarIncrements + 1, 1))
        self.pricePoints = {key / self.dollarIncrements: [] for key in keys}
        self.lastExecutedPrice = None
        self.market = market

    def getActiveOrders(self):
        r = {}
        for k,v in self.pricePoints.items():
            if len(v) > 0:
                r[k] = v
        return r

    def placeOrder(self, order: Order):
        if order.price > self.orderBookDepth or order.price < 0:
            print("invalid order placed: price not in range: ", price)
            return
        remainingOrder = self.matchOrder(order)
        self.pricePoints[order.price * 100].append(order)

    def matchOrder(self, order: Order):
        # Market order
        if order.orderType == 0:
            self.matchMarketOrder(order)
        else:
            self.matchLimitOrder(order)
        self.market.orderData.append(self.lastExecutedPrice)

    def matchMarketOrder(self, order: Order):
        price = self.lastExecutedPrice if self.lastExecutedPrice else (0.0 if order.buy else float(self.orderBookDepth))
        while not order.filled and not price < 0 and not price > self.orderBookDepth:
            orderList = self.pricePoints[price]
            if order.buy:
                for o in orderList:
                    if order.buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares -= order.shares

                            o.sharesChanged -= order.shares
                            o.amountChanged += order.shares * price
                            self.market.settleOrder(o)

                            order.sharesChanged += order.shares
                            order.amountChanged -= order.shares * price
                            

                            order.shares = 0
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
                            self.market.settleOrder(o)


                            self.lastExecutedPrice = price
                price += .01
                price = round(price,2)                
            else:
                for o in orderList:
                    if order.buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares += order.shares

                            o.sharesChanged += order.shares
                            o.amountChanged -= order.shares * price
                            self.market.settleOrder(o)

                            order.sharesChanged -= order.shares
                            order.amountChanged += order.shares * price

                            order.shares = 0
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
                            self.market.settleOrder(o)
                            
                            self.lastExecutedPrice = price
                price -= .01
                price = round(price,2)

        if not order.filled:
            print('Market ran out of liquidity!')

        self.market.settleOrder(order)
        

    def matchLimitOrder(self, order : Order):
        orderFilled = False
        price = self.lastExecutedPrice if self.lastExecutedPrice else (0.0 if order.buy else float(self.orderBookDepth))
        if order.buy:
            while not order.filled and not price < 0 and not price > self.orderBookDepth and price <= order.price:
                orderList = self.pricePoints[price]
                for o in orderList:
                    if order.buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares -= order.shares

                            o.sharesChanged -= order.shares
                            o.amountChanged += order.shares * price
                            self.market.settleOrder(o)

                            order.sharesChanged += order.shares
                            order.amountChanged -= order.shares * price

                            order.shares = 0
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
                            self.market.settleOrder(o)

                            self.lastExecutedPrice = price
                price += .01
                price = round(price,2)
        else:
            while not order.filled and not price < 0 and not price > self.orderBookDepth and price >= order.price:
                orderList = self.pricePoints[price]
                for o in orderList:
                    if order.buy != o.buy:
                        if o.shares >= order.shares:
                            o.shares += order.shares

                            o.sharesChanged += order.shares
                            o.amountChanged -= order.shares * price
                            self.market.settleOrder(o)

                            order.sharesChanged -= order.shares
                            order.amountChanged += order.shares * price

                            order.shares = 0
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
                            self.market.settleOrder(o)
                            
                            self.lastExecutedPrice = price
                price -= .01
                price = round(price,2)

        self.market.settleOrder(order)

        if not orderFilled:
            self.insertInOrderbook(order)


    def insertInOrderbook(self, order : Order):
        self.pricePoints[order.price].append(order)
