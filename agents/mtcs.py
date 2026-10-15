import math
import random
import copy

class MCTSNode:
    def __init__(self, game_state, parent=None, move=None):
        self.game_state = game_state  # Instance of ConnectFour
        self.parent = parent
        self.move = move  # The move that led to this state
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.untried_moves = game_state.legal_moves()

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, c=1.41):
        # Select child using UCT formula
        choices_weights = [
            (child.wins / child.visits) + c * math.sqrt(2 * math.log(self.visits) / child.visits)
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]


class MCTS:
    def __init__(self, iterations=1000):
        self.iterations = iterations

    def search(self, initial_state):
        root = MCTSNode(copy.deepcopy(initial_state))
        root_player = initial_state.current_player

        for _ in range(self.iterations):
            node = root
            state = copy.deepcopy(initial_state)

            # 1. Selection
            while node.is_fully_expanded() and node.children:
                node = node.best_child()
                state.apply_move(node.move)

            # 2. Expansion
            if node.untried_moves and not state.check_win():
                move = random.choice(node.untried_moves)
                node.untried_moves.remove(move)
                state.apply_move(move) # advance state
                
                child_node = MCTSNode(copy.deepcopy(state), parent=node, move=move)
                node.children.append(child_node)
                node = child_node

            # 3. Simulation (Rollout)
            sim_state = copy.deepcopy(state)
            winner = sim_state.check_win()
            while not winner:
                legal_moves = sim_state.legal_moves()
                if not legal_moves:
                    break
                random_move = random.choice(legal_moves)
                sim_state.apply_move(random_move)
                winner = sim_state.check_win()

            # 4. Backpropagation
            while node is not None:
                node.visits += 1
                if winner == root_player:
                    node.wins += 1.0
                elif winner:
                    node.wins += 0.5  
                node = node.parent

        if not root.children:
            return random.choice(sim_state.legal_moves()) + 1
        
        best_child_node = max(root.children, key=lambda c: c.visits)
        
        # Return 1-7
        return best_child_node.move + 1