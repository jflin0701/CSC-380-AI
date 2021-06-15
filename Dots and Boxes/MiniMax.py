class Algorithm:

    # the function for miniMax algorithm
    def minimax(self, ply_num):

        # generating the children
        for i in range(self.current.board_y):
            for j in range(self.current.board_x):
                if self.current.board[i][j] == ' ' and (j, i) not in self.child:
                    self.create(j, i, True)

        min_value = 1000
        i = 0
        j = 0
        for k, l in self.child.items():
            result = Algorithm.maximum(l, ply_num - 1)
            if min_value > result:
                min_value = result
                i = k[0]
                j = k[1]
        return i, j

    def maximum(self, ply_num):
        if ply_num == 0:
            return self.cur_score

        # generating the children
        for i in range(self.current.board_y):
            for j in range(self.current.board_x):
                if self.current.board[i][j] == ' ' and (j, i) not in self.child:
                    self.create(j, i, False)
        max_value = -1000
        for k, l in self.child.items():
            result = Algorithm.minimum(l, ply_num - 1)
            if max_value < result:
                max_value = result
        return max_value

    def minimum(self, ply_num):
        if ply_num == 0:
            return self.cur_score

        # generating the children
        for i in range(self.current.board_y):
            for j in range(self.current.board_x):
                if self.current.board[i][j] == ' ' and (j, i) not in self.child:
                    self.create(j, i, True)
        min_value = 1000
        for k, l in self.child.items():
            result = Algorithm.maximum(l, ply_num - 1)
            if min_value > result:
                min_value = result
        return min_value
