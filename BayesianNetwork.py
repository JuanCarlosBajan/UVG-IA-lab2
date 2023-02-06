import warnings

class Node:
    def __init__(self, title: str, probability_of_success:float = None):
        self.title = title
        self.connections = []

        if probability_of_success is not None:
            if probability_of_success > 1 or probability_of_success < 0:
                raise ValueError("This probability of success is wrong")

            self.success = probability_of_success
            self.fail = 1 - probability_of_success
        else:
            self.success = None
            self.fail = None

    def add_connection(self, next_node_title:str, probability_of_success:float, parent_was_succesful:bool):
        connection = list(
                        filter(
                            lambda x: 
                                next_node_title == x['title'] and 
                                parent_was_succesful == x['parent_success'], 
                            self.connections
                            )
                        )
        if probability_of_success > 1 or probability_of_success < 0:
            print('Probability "' + str(probability_of_success) + '" cant be used.')
            return False
        
        if type(parent_was_succesful) != bool:
            print('You need to provide true or false depending on wether the parent was succesful or not')
            return False
        
        if not connection:
            self.connections.append({
                'title': next_node_title,
                'parent_success': parent_was_succesful,
                'success':probability_of_success,
                'fail': 1-probability_of_success
            })
            return True
        
        else: 
            print('The node "' + self.title + '" already has a connection to "' + next_node_title + '"')
            return False

    def get_children(self):
        return self.connections
    
    def get_children_title(self):
        return list(
                    set(
                        [connection['title'] for connection in self.connections]
                        )
                    )
    
    def delete_connection(self, node_title:str):
        before_i = len(self.connections)
        self.connections = list(
                                filter(
                                    lambda connection: 
                                        node_title != connection['title'], 
                                    self.connections
                                    )
                                )
        
        if(before_i == len(self.connections)):
            print('There is no connection from node "' + self.title + '" to node "' + node_title + '".')
            return False
        
        return True
    
    def delete_connection(self, node_title:str, parent_was_succesful:bool):
        before_i = len(self.connections)
        self.connections = list(
                                filter(
                                    lambda connection: 
                                        node_title != connection['title'] and 
                                        parent_was_succesful != connection['parent_success'], 
                                    self.connections
                                    )
                                )
        
        if(before_i == len(self.connections)):
            print('There is no connection from node "' + self.title + '" to node "' + node_title + '".')
            return False
        
        return True

    def edit_connection(self, node_title:str, probability_of_success:float):
        res = self.delete_connection(node_title)
        if res:    
            res = self.add_connection(node_title, probability_of_success)
        return res

class BayesianNetwork:
    def __init__(self):
        self.nodes = []

    def get_nodes(self):
        return self.nodes
    
    def get_node(self, node_title: str):
        return list(
                    filter(
                        lambda node: 
                            node_title == node.title,
                        self.nodes
                    )
                )[0]  

    def delete_node(self, node_title:str):
        before_i = len(self.nodes)
        self.nodes = list(
                        filter(
                            lambda node: 
                                node_title != node.title,
                            self.nodes
                            )
                        )
        if before_i == len(self.nodes):
            print('No nodes with title "' + node_title + '" were found.')
            return False
        return True

    def add_node(self, node:Node):
        nodes = list(
                    filter(
                        lambda x: 
                            node.title == x.title,
                        self.nodes
                        )
                    )
        if not nodes:
            self.nodes.append(node)
            return True
        else:
            print('Node "' + node.title + '" already exists on network')
            return False

    def replace_node(self, node_title:str, new_node:Node):
        res = self.delete_node(node_title)
        if res:
            self.add_node(new_node)
        return res

    def get_parents(self, child_node_title:str):
        return list(
            set(
                filter(
                    lambda node: 
                        child_node_title in node.get_children_title(), 
                    self.nodes
                )
            )
        )

    def probabilistic_inference(self, node_title:str):
        current_node = self.get_node(node_title)

        if current_node.success is not None: 
            return {
                'success': current_node.success,
                'fail': current_node.fail
            }
        
        parents = self.get_parents(node_title)
        parents_title = [parent.title for parent in parents]
        connections = []

        for parent in parents:

            parent_probability = self.probabilistic_inference(parent.title)

            found_connections = list(
                filter(
                    lambda connection:
                    connection['title'] == node_title,
                    parent.connections
                )
            )

            for connection in found_connections:
                connection['parent'] = parent.title

            connections += found_connections
        
        if len(connections) < len(parents)*2:
            print('The amount of connections parents have to node "' + node_title + '" arent enough.\n You are missing ' + str(len(parents)*2 - len(connections)) + " connections.")

        for parent in parents:


node_a = Node('a',0.6)
node_a.add_connection('b',0.4,True)
node_a.add_connection('b',0.4,False)

node_b = Node('b')
node_b.add_connection('c',0.5, True)
node_b.add_connection('c',0.5, False)

node_c = Node('c')
node_c.add_connection('d',0.3,True)
node_c.add_connection('d',0.8,False)

node_c_replace = Node('c')
node_c_replace.add_connection('d',0.4,True)
node_c_replace.add_connection('d',0.7,False)

network = BayesianNetwork()
network.add_node(node_a)
network.add_node(node_b)
network.add_node(node_c)

print(network.probabilistic_inference('b'))

