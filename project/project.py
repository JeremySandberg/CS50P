#Path finding algorithm
"""
Asks for board size nxn
Asks for random amount of blocks
Randomly places blocks
Finds a path from top left corner to bottom right
Draws board and path
Can step orthogonal and diagonal
"""
import numpy as np
import matplotlib.pyplot as plt

class Node():
    #Node class for Pathfinding

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __add__(self, other):
        return (self.position[0]+other[0], self.position[1]+other[1])

def main():
    while True:
        try:
            size = int(input("Board side length: "))
            if size < 0:
                raise ValueError
            break
        except:
            print("Invalid input")

    while True:
        try:
            blocks = int(input("Amount of blockages: "))
            if blocks < 0 or blocks >= size**2-2:
                raise ValueError
            break
        except:
            print("Invalid input")

    board = create_board(size)
    populated = populate_board(board, size, blocks)
    path = find_path(populated, (0,0), (size-1, size-1))
    draw_path(populated, path)

def create_board(size):
    return np.zeros((size, size), dtype=int)

def populate_board(board, size, blocks):
    np.random.seed(12345)
    for i in np.random.choice(range(1,size*size-1), blocks, replace=False):
        board[i//size][i%size] = 1
    return board

def find_path(board, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = [start_node]
    closed_list = []

    while len(open_list) > 0:
        current_node = open_list[0]
        current_i = 0

        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_i = i

        open_list.pop(current_i)
        closed_list.append(current_node)

        if current_node == end_node:
            path_x = []
            path_y = []
            current = current_node
            while current is not None:
                x, y = current.position
                path_x.append(x)
                path_y.append(y)
                current = current.parent
            return (path_x[::-1], path_y[::-1])

        children = []
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_move = current_node + move

            if node_move[0] > (len(board) - 1) or node_move[0] < 0:
                continue
            if node_move[1] > (len(board) - 1) or node_move[1] < 0:
                continue
            if board[node_move[0]][node_move[1]] != 0:
                continue

            new_node = Node(current_node, node_move)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)

def draw_path(board=None, path=None):
    plt.matshow(board, cmap='Greys')
    if path is not None:
        y, x = path
        plt.plot(x, y)
    plt.xticks([])
    plt.yticks([])
    plt.savefig("figure1.png")


if __name__ == "__main__":
    main()