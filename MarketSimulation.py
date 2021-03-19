from src.Market import Market
from src.Agent import Agent
from src.Order import Order
from src.AgentFactory import AgentFactory
import uuid
import threading
#initialize some limit sell orders for liquidity

master = Agent(riskPropensity=.1, buyingPower=1000, shares=10000)

af = AgentFactory()
agents = af.createAgents(10)
agents[master.id] = master

m = Market(agents)

master.placeOrder(orderType=1, buy=False, shares=1000, price=20.0)
master.placeOrder(orderType=1, buy=False, shares=1000, price=21.0)
master.placeOrder(orderType=1, buy=False, shares=1000, price=22.0)
master.placeOrder(orderType=1, buy=False, shares=1000, price=50.0)
master.placeOrder(orderType=1, buy=False, shares=1000, price=100.0)
master.placeOrder(orderType=1, buy=False, shares=1000, price=500.0)

while True:
    for a in agents.values():
        a.policy()
        print(m.getCurrentPrice())



