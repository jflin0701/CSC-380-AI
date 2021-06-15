from Game import *

# MiniMax algorithm for Dots and Boxes
# Jia Feng Lin (Jeffrey)


def main():
    while True:
        print("Dots and Boxes")
        board_x = int(input("Enter rows: "))
        board_x = board_x * 2 + 1
        if board_x < 5:
            print("Please enter at least 2")
            exit()
        board_y = int(input("Enter columns: "))
        board_y = board_y * 2 + 1
        if board_y < 5:
            print("Please enter at least 2")
            exit()
        ply_num = int(input("Enter plies: "))
        if ply_num < 2:
            print("Please enter greater than 1")
            exit()
        match = DotsNBoxes(board_x, board_y, ply_num)
        match.start()


if __name__ == '__main__':
    main()
