from src.Market import Market
from src.Agent import Agent
from src.Order import Order
import uuid

agent = Agent(.1, 1000)
#order = 
m = Market({agent.id : agent})
agent.placeOrder(order)



