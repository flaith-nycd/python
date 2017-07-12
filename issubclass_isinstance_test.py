from heritage_test import *

print(issubclass(AgentSpecial, Personne))  # AgentSpecial hérite de Personne
# True
print(issubclass(AgentSpecial, object))
# True
print(issubclass(Personne, object))
# True
print(issubclass(Personne, AgentSpecial))  # Personne n'hérite pas d'AgentSpecial
# False

agent = AgentSpecial("Fisher", "18327-121")
print(isinstance(agent, AgentSpecial))  # Agent est une instance d'AgentSpecial
# True
print(isinstance(agent, Personne))  # Agent est une instance héritée de Personne
# True
