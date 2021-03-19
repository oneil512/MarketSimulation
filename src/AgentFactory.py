import random
from src.Agent import Agent

class AgentFactory:
    def createAgents(self, n : int):
        agentDict = {}
        for i in range(n):
            agent = Agent(riskPropensity=random.random(), buyingPower=random.randint(1000, 5000))
            agentDict[agent.id] = agent
        return agentDict