from src.Market import Market
from src.Agent import Agent
from src.Order import Order
import uuid
#initialize some limit sell orders for liquidity

agent1 = Agent(riskPropensity=.1, buyingPower=1000, shares=20)
agent2 = Agent(riskPropensity=.1, buyingPower=1000, shares=1)
m = Market({agent1.id : agent1, agent2.id : agent2})
agent1.placeOrder(orderType=1, buy=False, shares=10, price=0.01)
agent2.placeOrder(orderType=1, buy=True, shares=10, price=0.01)
print(m.getCurrentPrice())



