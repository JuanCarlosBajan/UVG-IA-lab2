class Node:
    def __init__(self, title, probability = None):
        self.title = title
        self.connections = []
        self.probability = probability

    def add_connection(self, next_node_title, probability_of_success):
        connection = list(filter(lambda x: next_node_title == x.title, self.connections))
        if probability_of_success > 1:
            print('Probability "' + str(probability_of_success) + '" cant be used.')
        if not connection:
            self.connections.append({
                'title': next_node_title,
                'success':probability_of_success,
                'fail': 1-probability_of_success
            })
        else: print('The node "' + next_node_title + '" is already on the network.')

    def get_children(self):
        return self.connections
    
    def get_children_title(self):
        return [connection.title for connection in self.connections]
    
    def delete_connection(self, node_title):
        self.connections = list(filter(lambda connection: node_title != connection.title, self.connections))

    def edit_connection(self, node_title, probability_of_success):
        self.delete_connection(node_title)
        self.add_connection(node_title, probability_of_success)

class BayesianNetwork:
    def __init__(self):
        self.nodes = []

    def get_nodes(self):
        return self.nodes
    
    def delete_node(self, node_title):
        self.nodes = list(filter(lambda node: node_title != node.title, self.nodes))

    def add_node(self, node):
        self.nodes.append(node)

    def replace_node(self, node_title, new_node):
        self.delete_node(node_title)
        self.add_node(new_node)

    def get_parents(self, child_node_title):
        return list(
            filter(
                lambda node: child_node_title in node.get_children_title(), self.nodes
            )
        )
