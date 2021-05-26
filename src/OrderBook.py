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

    def matchOrder(self, order: Order):
        if order.orderType == 0:
            order, price = self.matchMarketOrder(order)
        else:
            order, price = self.matchLimitOrder(order)

        if not order.filled:
            if price < 0:
                price = 0.0

            if price > self.orderBookDepth:
                price = self.orderBookDepth

            if order.orderType == 1:
                self.insertInOrderbook(order)
            else:
                print('Market ran out of liquidity!')

        self.lastExecutedPrice = price
        self.market.settleOrder(order)
        self.market.orderData.append(self.lastExecutedPrice)

    def matchLimitOrder(self, order):
        price = order.price
        orderList = self.pricePoints[price]
        return self.execute_order(order, orderList, price)

    def matchMarketOrder(self, order):
        price = self.lastExecutedPrice if self.lastExecutedPrice else (0.0 if order.buy else float(self.orderBookDepth))
        while not order.filled and not price < 0 and not price > self.orderBookDepth:
            orderList = self.pricePoints[price]
            order, price = self.execute_order(order, orderList, price)
            if order.filled:
                break

            price += .01 if order.buy else -.01
            price = round(price,2)
        return order, price


    def insertInOrderbook(self, order : Order):
        self.pricePoints[order.price].append(order)


    def execute_order(self, order, orderList, price):
        buy_flag = 1 if order.buy else -1
        for o in orderList:
            if order.buy != o.buy:
                if o.shares >= order.shares:
                    o.shares -= order.shares

                    o.sharesChanged -= order.shares * buy_flag
                    o.amountChanged += order.shares * price * buy_flag

                    order.sharesChanged += order.shares * buy_flag
                    order.amountChanged -= order.shares * price * buy_flag

                    order.shares = 0
                    order.filled = True
                    break
                else:
                    order.shares -= o.shares
                    o.sharesChanged -= o.shares * buy_flag
                    o.amountChanged += o.shares * price * buy_flag

                    order.sharesChanged += o.shares * buy_flag
                    order.amountChanged -= o.shares * price * buy_flag

                    o.shares = 0
                    o.filled = True

                self.market.settleOrder(o)

        return order, price