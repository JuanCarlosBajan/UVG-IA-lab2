# example.py
from bayesian_library import BayesianNetwork, Node

# Crear una nueva red bayesiana
bn = BayesianNetwork()

# Agregar nodos a la red bayesiana
cloudy = bn.add_node("cloudy", ["yes", "no"])
sprinkler = bn.add_node("sprinkler", ["yes", "no"])
rain = bn.add_node("rain", ["yes", "no"])
wet_grass = bn.add_node("wet_grass", ["yes", "no"])

# Definir relaciones entre los nodos
bn.set_relation(cloudy, sprinkler)
bn.set_relation(cloudy, rain)
bn.set_relation(sprinkler, wet_grass)
bn.set_relation(rain, wet_grass)

# Establecer distribuciones de probabilidad para cada nodo
bn.set_probability(cloudy, "yes", 0.5)
bn.set_probability(cloudy, "no", 0.5)
bn.set_probability(sprinkler, "yes", 0.1)
bn.set_probability(sprinkler, "no", 0.9)
bn.set_probability(rain, "yes", 0.8)
bn.set_probability(rain, "no", 0.2)
bn.set_probability(wet_grass, "yes", {
                   "yes": {"yes": 0.99, "no": 0.9}, "no": {"yes": 0.9, "no": 0.0}})
bn.set_probability(wet_grass, "no", {
                   "yes": {"yes": 0.01, "no": 0.1}, "no": {"yes": 0.1, "no": 1.0}})

# Realizar inferencia probabilística
evidence = {"cloudy": "yes", "sprinkler": "yes"}
target = wet_grass
result = bn.inference(target, evidence)
print("Probabilidad de tener pasto mojado dado que está nublado y el riego está encendido:", result)
