from bayesian_networks_rey20074 import BayesianNetwork

node_b = BayesianNetwork.Node('b', 0.001)

node_e = BayesianNetwork.Node('e', 0.002)

node_a = BayesianNetwork.Node('a', multiple_parents=True)
node_a.add_connection_multiple_parents({'b': True, 'e': True}, 0.95)
node_a.add_connection_multiple_parents({'b': True, 'e': False}, 0.94)
node_a.add_connection_multiple_parents({'b': False, 'e': True}, 0.29)
node_a.add_connection_multiple_parents({'b': False, 'e': False}, 0.001)
node_a.add_connection('j', 0.9, True)
node_a.add_connection('j', 0.05, False)
node_a.add_connection('m', 0.7, True)
node_a.add_connection('m', 0.01, False)

node_j = BayesianNetwork.Node('j')
node_m = BayesianNetwork.Node('m')


network = BayesianNetwork.BayesianNetwork()
network.add_node(node_a)
network.add_node(node_b)
network.add_node(node_e)
network.add_node(node_j)
network.add_node(node_m)

print(network.probabilistic_inference('m'))
