class Node:
    def __init__(self, cur_state):
        # current state of the board
        self.current = cur_state
        # current score of the game
        self.cur_score = 0
        # contains the child
        self.child = {}

    # create child node
    def create(self, i, j, player):
        self.child[(i, j)] = Node(self.current.get_state())
        mul = 1
        if player:
            mul *= -1
        self.child[(i, j)].cur_score = (self.child[(i, j)].current.action(i, j) * mul) + self.cur_score

    # function to generate the board
    def draw(self):
        self.current.draw_board()
