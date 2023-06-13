import math
import numpy as np
import torch


class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.value = 0
        self.is_expanded = False


class MCTS:
    def __init__(self, neural_network, n_simulations=800, c_puct=1.0):
        self.neural_network = neural_network
        self.n_simulations = n_simulations
        self.c_puct = c_puct

    def select_child(self, node, state):

        policy, _ = self.evaluate(state)

        def ucb_score(parent_node, action):
            child_node = parent_node.children[action]
            p = math.sqrt(parent_node.visits) * (1 + np.random.randn() * 0.0001)
            u = self.c_puct * p * policy[action] / (1 + child_node.visits)
            return child_node.value + u

        return max(node.children.items(), key=lambda item: ucb_score(node, item[0]))

    def evaluate(self, state):
        board = torch.FloatTensor(state.board).unsqueeze(0).unsqueeze(0)
        with torch.no_grad():
            policy, value = self.neural_network(board)
        return policy.numpy(), value.item()

    def backpropagate(self, search_path, value):
        for node in reversed(search_path):
            node.visits += 1
            node.value += value
            value = -value

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def search(self, game):
        """Perform the MCTS search to find the best action for a given game state."""
        root = Node()

        # Perform simulations
        for _ in range(self.n_simulations):
            state_copy = game.copy()
            node = root
            search_path = [node]

            # Selection phase
            while node.is_expanded:
                action, node = self.select_child(node, state_copy)
                state_copy.make_move(action)
                search_path.append(node)

            # Expansion and Evaluation phase
            policy, value = self.evaluate(state_copy)
            node.is_expanded = True
            node.children = {action: Node(parent=node)
                             for action in state_copy.get_valid_moves()}

            # Backpropagation phase
            self.backpropagate

    def select_action(self, node, temperature):
        actions = list(node.children.keys())
        if temperature == 0:
            return max(actions, key=lambda a: node.children[a].value)
        values = np.array([child.value for child in node.children.values()])
        probs = self.softmax(values / temperature)
        return np.random.choice(actions, p=probs)