from src.Market import Market
from src.Agent import Agent
from src.Order import Order
from src.AgentFactory import AgentFactory
import uuid
import threading
#initialize some limit sell orders for liquidity

master = Agent(riskPropensity=.1, buyingPower=1000, shares=10000)

af = AgentFactory()
agents = af.createAgents(100)
agents[master.id] = master

m = Market(agents)

master.placeOrder(orderType=1, buy=False, shares=200, price=20.0)
master.placeOrder(orderType=1, buy=False, shares=100, price=21.0)
master.placeOrder(orderType=1, buy=False, shares=50, price=22.0)

master.placeOrder(orderType=1, buy=True, shares=5, price=19.0)
master.placeOrder(orderType=1, buy=True, shares=10, price=18.0)
master.placeOrder(orderType=1, buy=True, shares=20, price=17.0)

while True:
    for a in agents.values():
        if not a is master:
            a.policy_2()
            print(m.getCurrentPrice())



