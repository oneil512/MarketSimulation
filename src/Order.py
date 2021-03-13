import uuid

class Order:

    def __init__(self, orderType: int, buy: bool, price: float, shares: int, id_: uuid.uuid4, amountPaid: float):
        self.orderType = orderType # 0 is market 1 is limit
        self.buy = buy
        self.price = price
        self.amountPaid = amountPaid
        self.shares = shares
        self.filled = False
        self.agentId  = id_
        self.sharesChanged = 0
        self.amountChanged = 0
