from Board import *
from Node import *
from MiniMax import *


class DotsNBoxes:
    def __init__(self, board_x, board_y, ply_num):
        cur_state = Game([], board_x, board_y)
        cur_state.initiate()
        # create node with the current state
        self.state = Node(cur_state)
        # number of plies
        self.ply_num = ply_num

    # starts the game with human as first move
    def start(self):
        self.human()

    # human's turn
    def human(self):
        self.state.draw()
        print("Your turn!")
        print("Enter x,y:")
        human_x = int(input("x: "))
        human_y = int(input("y: "))

        if (human_x, human_y) not in self.state.child:
            self.state.create(human_x, human_y, False)
            self.state = self.state.child[(human_x, human_y)]
        else:
            self.state = self.state.child[(human_x, human_y)]

        print("Current Score: " + str(self.state.cur_score))

        self.ai()

    # ai's turn
    def ai(self):

        self.state.draw()
        print("AI's turn!")
        move = Algorithm.minimax(self.state, self.ply_num)
        self.state = self.state.child[(move[0], move[1])]
        print("AI's move: (" + str(move[0]) + "," + str(move[1]) + ")")
        print("Current Score: " + str(self.state.cur_score))

        if len(self.state.child) == 0:
            self.state.draw()
            self.eval()
            return

        self.human()

    # evaluate the final score
    def eval(self):
        print("Good Game!")
        if self.state.cur_score > 0:
            print("You won!")
            exit()
        elif self.state.cur_score < 0:
            print("You lost!")
            exit()
        else:
            print("Draw")
            exit()
