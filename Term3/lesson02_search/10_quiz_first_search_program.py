# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    # print('closed[{}][{}]'.format(len(closed), len(closed[0])))
    # print('grid[{}][{}]'.format(len(grid), len(grid[0])))

    g = 0 
    x = init[0]
    y = init[1]
    
    open_list = [[g, x, y]]
    # print('initial open list:')
    # for open_item in open_list:
    #     print(open_item)
    # print('----')

    found = False
    resign = False

    result = 'fail'
    while not found and not resign:
        if len(open_list) == 0:
            resign = True
            print("resign! could'nt find path")
        else:
            
            open_list.sort()
            open_list.reverse()
            next_item = open_list.pop()
            
            # print('take list item')
            # print(next_item)

            g = next_item[0]
            x = next_item[1]
            y = next_item[2]

            if x == goal[0] and y == goal[1]:
                found = True
                # print('found goal')
                # print(next_item)
                result = next_item
            else:
                for direction in delta:
                    x2 = x + direction[0]
                    y2 = y + direction[1]

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            new_item = [g2, x2, y2]
                            open_list.append(new_item)
                            # print('append list item')
                            # print(new_item)
                            closed[x2][y2] = 1

            # print('new open list:')
            # for open_item in open_list:
            #     print(open_item)
            # print('----')
    
    return result
print(search(grid,init,goal,cost))
