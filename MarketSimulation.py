from src.Market import Market
from src.Agent import Agent
from src.Order import Order
import uuid
#initialize some limit sell orders for liquidity

agent = Agent(riskPropensity=.1, buyingPower=1000, shares=1)
m = Market({agent.id : agent})
agent.placeOrder(orderType=1, buy=True, shares=1, price=1.0)
m.getCurrentPrice()



