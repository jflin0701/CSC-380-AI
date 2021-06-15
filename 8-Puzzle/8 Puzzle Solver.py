#********************************#
# Search Alogrithms for 8-puzzle #
#                                #
#     Jia Feng Lin (Jeffrey)     #
#                                #
#********************************#
#
#
# The state of the board is stored in a 2D array.
# The 0 denotes the blank space.
#
# goal = np.array([[1,2,3],
#                  [8,0,4],
#                  [7,6,5]])
#
#
#

import numpy as np # used to store the puzzle in an array
import time

# Node structure
class Node:
    def __init__(self, state, parent, action, depth, cost):
        # Contains the state of the node
        self.state = state
        # Contains the parent node
        self.parent = parent
        # Contains the action
        self.action = action
        # Contains the depth of node
        self.depth = depth
        # Contains the cost of action
        self.cost = cost
        # Heuristis
        self.h1 = None
        # Manhattan
        self.h2 = None

# Get the position of zero
def get_index(puzzle):
    x,y = np.where(puzzle == 0)
    x = int(x)
    y = int(y)
    return x,y

# Swap 0 to the left, and return the cost of move
def left(state):
    x,y = get_index(state)
    cost = 0
    new_state = []
    if y == 0:
        return None
    else:
        temp_state = np.copy(state)
        temp = temp_state[x,y-1]
        temp_state[x,y] = temp
        cost = temp_state[x,y-1] 
        temp_state[x,y-1] = 0
        new_state.append(temp_state)
        new_state.append(cost)
    return new_state
# Swap 0 to the right, and return the cost of move
def right(state):
    x,y = get_index(state)
    cost = 0
    new_state = []
    if y == 2:
        return None
    else:
        temp_state = np.copy(state)
        temp = temp_state[x,y+1]
        temp_state[x,y] = temp
        cost = temp_state[x,y+1]
        temp_state[x,y+1] = 0
        new_state.append(temp_state)
        new_state.append(cost)
    return new_state

# Swap 0 to the up, and return the cost of move
def up(state):
    x,y = get_index(state)
    cost = 0
    new_state = []
    if x == 0:
        return None
    else:
        temp_state = np.copy(state)
        temp = temp_state[x-1,y]
        temp_state[x,y] = temp
        cost = temp_state[x-1,y]
        temp_state[x-1,y] = 0
        new_state.append(temp_state)
        new_state.append(cost)
    return new_state

# Swap 0 to the down, and return the cost of move
def down(state):
    x,y = get_index(state)
    cost = 0
    new_state = []
    if x == 2:
        return None
    else:
        temp_state = np.copy(state)
        temp = temp_state[x+1,y]
        temp_state[x,y] = temp
        cost = temp_state[x+1,y]
        temp_state[x+1,y] = 0
        new_state.append(temp_state)
        new_state.append(cost)
    return new_state
    
moves = ['Left','Right','Up','Down']

# Moving action 
def move_action(action, state):    
    if action == 'Right':
        return left(state)
    elif action == 'Left':
        return right(state)
    elif action == 'Down':
        return up(state)
    elif action == 'Up':
        return down(state)

# Printing the path
def result(lst):
    print('Result: ')
    if lst == None:
        print('No solution was found')
        return
    path = lst[0]
    length = len(path)
    cost = 0
    for i in path:
        cost += i.cost
        print('Move: {} \nResult: \n{} \nCost: {} \nDepth: {} \n------------'
                .format(str(i.action),str(i.state),str(i.cost),str(i.depth)))
    print('\nLength: {} \nCost: {} \
          \nTime: {} \nSpace: {}'.format(str(length),str(cost),str(lst[1]),str(lst[2])))

# Node creation function
def create_node(state, parent, action, depth, cost):
    return Node(state, parent, action, depth, cost)

# Return list of child nodes
def expand_node(node):
    expanded_nodes = []
    for move in moves:
        state = move_action(move,node.state)
        # Filter out moves that cannot be made
        if state is not None:
            new_state = state[0]
            cost = state[1]
            expanded_nodes.append(create_node(new_state, node, move, node.depth + 1, cost))
    return expanded_nodes

# Breadth-First search
def bfs(node, goal):

    queue = [node]
    current_node = queue.pop(0)
    result = []
    path = []
    time = 1
    space = 1
    while(current_node.state.tolist() != goal.tolist()):
        # adding all child nodes to queue
        queue.extend(expand_node(current_node))
        current_node = queue.pop(0)
        time += 1
    # create list of path from goal node to root
    while(current_node.parent != None):
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result

# Depth-First search
def dfs(node, goal):

    queue = [node]
    current_node = queue.pop()
    visited = []
    result = []
    path = []
    time = 1
    space = 1
    while(current_node.state.tolist() != goal.tolist()):
        temp = expand_node(current_node)
        # adding all child nodes to queue
        for child in temp:              
            queue.insert(0,child)
            if child not in visited:
                visited.append(child)
            else:
                queue.pop(child)
        current_node = queue.pop()
        time += 1
        if current_node.depth > 10:
            return None
    # create list of path from goal node to root
    while(current_node.parent != None): 
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result

# Uniform cost Search
def ucs(node, goal):

    queue = [node]
    current_node = queue.pop(0)
    result = []
    path = []
    time = 1
    space = 1
    while(current_node.state.tolist() != goal.tolist()):
        temp = expand_node(current_node)
        # adding all child nodes to queue
        for child in temp:
            child.depth += current_node.depth
            queue.append(child)
        # sorting the queue by depth
        queue.sort(key = lambda n: n.depth)
        current_node = queue.pop(0)
        time += 1
    # create list of path from goal node to root
    while(current_node.parent != None):
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result

# Greedy Best First Search
def gbf(node, goal):

    queue = [node]
    current_node = queue.pop(0)
    result = []
    path = []
    time = 1
    space = 0
    while(current_node.state.tolist() != goal.tolist()):
        # adding all child nodes to queue
        queue.extend(expand_node(current_node))
        for item in queue:
            h1(item,goal)
        # sorting the queue by heuristics
        queue.sort(key = lambda h: h.h1)
        current_node = queue.pop(0)
        time += 1
    # create list of path from goal node to root
    while(current_node.parent != None):
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result
            
# A* Search with h1
def a_search(node, goal):
    
    queue = [node]
    current_node = queue.pop(0)
    result = []
    path = []
    time = 1
    space = 1
    while(current_node.state.tolist() != goal.tolist()):
        # adding all child nodes to queue
        queue.extend(expand_node(current_node))
        for item in queue:
            h1(item,goal)
            item.h1 += item.depth
        # sorting the queue by heuristics
        queue.sort(key = lambda h: h.h1)
        current_node = queue.pop(0)
        time += 1
    # create list of path from goal node to root
    while(current_node.parent != None): 
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result

# A* Search with h2
def a_search_h2(node, goal):
    
    queue = [node]
    current_node = queue.pop(0)
    result = []
    path = []
    time = 1
    space = 1
    while(current_node.state.tolist() != goal.tolist()):
        # adding all child nodes to queue
        queue.extend(expand_node(current_node))
        for item in queue:
            h2(item,goal)
        # sorting the queue by manhattan
        queue.sort(key = lambda h: h.h2)
        current_node = queue.pop(0)
        time += 1
    # create list of path from goal node to root
    while(current_node.parent != None): 
        path.insert(0,current_node)
        current_node = current_node.parent
    space = len(queue) + time
    result.append(path)
    result.append(time)
    result.append(space)
    return result
    
# Heuristics
# number of misplaced tiles
def h1(state, goal):
    misplaced = 0
    for x in range(0,3):
        for y in range(0,3):
            if state.state[x][y] != goal[x][y]:
                misplaced += 1
    state.h1 = misplaced

# Manhattan
# sum of the distances of every tile to its goal
def h2(state, goal):
    manhat = 0
    for i in range(1,9):
        x,y = np.where(state.state == i)
        i,j = np.where(goal == i)
        if x != i or y != j:
            manhat += abs(i-x)
            manhat += abs(j-y)
    state.h2 = manhat

# Main method
# program menu
def main():

    goal = np.array([[1,2,3],[8,0,4],[7,6,5]])
    easy_puzzle = np.array([[1,3,4],[8,6,2],[7,0,5]])
    med_puzzle = np.array([[2,8,1],[0,4,3],[7,6,5]])
    hard_puzzle = np.array([[5,6,7],[4,0,8],[3,2,1]])
    stop = 1
    while stop != 0:
        print('\nEnter 0 to exit!')
        print('1: Easy \n2: Medium \n3: Hard')
        puzzle = int(input('Pick puzzle: '))
        if puzzle == 1:
            root = Node(easy_puzzle,None,None,0,0)
        elif puzzle == 2:
            root = Node(med_puzzle,None,None,0,0)
        elif puzzle == 3:
            root = Node(hard_puzzle,None,None,0,0)
        else:
            stop = 0
            break

        print('\n1: Breadth first search \n2: Depth first search \
               \n3: Uniform cost search \n4: Greedy best first search\
               \n5: A* search with Heuristics\n6: A* search with Manhattan')
        search = int(input('Pick search: '))
        if search == 1:
            print('\nBreadth first search \n**********')
            start_time = time.time()
            result(bfs(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        elif search == 2:
            print('\nDepth first search \n**********')
            start_time = time.time()
            result(dfs(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        elif search == 3:
            print('\nUniform cost search \n**********')
            start_time = time.time()
            result(ucs(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        elif search == 4:
            print('\nGreedy Best first search \n**********')
            start_time = time.time()
            result(gbf(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        elif search == 5:
            print('\nA* search with Heuristics \n**********')
            start_time = time.time()
            result(a_search(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        elif search == 6:
            print('\nA* search with Manhattan \n**********')
            start_time = time.time()
            result(a_search_h2(root,goal))
            print('Run time: {}s'.format(str(time.time()-start_time)))
        else:
            stop = 0
        
main()
    

















































