class Order:

    def __init__(self, orderType: int, buy: bool, price: float, shares: int):
        self.orderType = orderType # 0 is market 1 is limit
        self.buy = buy
        self.price = price
        self.shares = shares
        self.filled = False
