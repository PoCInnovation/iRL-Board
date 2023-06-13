from mcts import MCTS

class AlphaZeroPlayer:
    def __init__(self, net, n_simulations=800, c_puct=1.0, temperature=1.0):
        self.mcts = MCTS(net, n_simulations=n_simulations, c_puct=c_puct)
        self.temperature = temperature

    def select_move(self, game):
        return self.mcts.search(game)
