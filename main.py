from src.bayesian_networks_rey20074.BayesianNetwork import Node, BayesianNetwork

node_b = Node('b', 0.001)

node_e = Node('e', 0.002)

node_a = Node('a', multiple_parents=True)
node_a.add_connection_multiple_parents({'b': True, 'e': True}, 0.95)
node_a.add_connection_multiple_parents({'b': True, 'e': False}, 0.94)
node_a.add_connection_multiple_parents({'b': False, 'e': True}, 0.29)
node_a.add_connection_multiple_parents({'b': False, 'e': False}, 0.001)
node_a.add_connection('j', 0.9, True)
node_a.add_connection('j', 0.05, False)
node_a.add_connection('m', 0.7, True)
node_a.add_connection('m', 0.01, False)

node_j = Node('j')
node_m = Node('m')


network = BayesianNetwork()
network.add_node(node_a)
network.add_node(node_b)
network.add_node(node_e)
network.add_node(node_j)
network.add_node(node_m)

print(network.probabilistic_inference('m'))
