import numpy as np
import uuid

class Agent:
    # riskPropensity: float 0-1, 1 is highest risk
    # buyingPower: int 0-some number
    def __init__(self, riskPropensity: float, buyingPower:int, market:Market):
        self.riskPropensity = riskPropensity
        self.buyingPower = buyingPower
        self.timePreference = self.getTimePreference()
        self.market = market
        self.id = uuid.uuid4()
        self.shares = 0


    # Returns time preference in seconds
    # Range from 30 seconds to a month (2.6 million seconds)
    def getTimePreference(self) -> int:
        return (((self.riskPropensity - 0.0) * (2.6 * 10 ** 6 - 30)) / (1.0 - 0.0)) + 30

    def getTrendPreference() -> np.array:
        marketData = this.market.getMarketData(this.timePreference)
        return marketData

