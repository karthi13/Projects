__author__ = 'yuafan'

import random
import numpy as np
import matplotlib.pyplot as plt
import Queue


sizeOfMap2D = [100, 50]
percentOfObstacle = 0.9  # 30% - 60%, random
q = Queue


# Generate 2D matrix of size x * y
# starting Point and Ending Point
def generateMap2d(size_):
# Generates a random 2d map of size size_. You can choose your desired size but whatever solution you come up with has
# to work independently of map size
    size_x, size_y = size_[0], size_[1]
    map2d = np.random.rand(size_y, size_x)
    perObstacles_ = percentOfObstacle
    map2d[map2d <= perObstacles_] = 0
    map2d[map2d > perObstacles_] = -1
    yloc, xloc = [np.random.random_integers(0, size_x-1, 2), np.random.random_integers(0, size_y-1, 2)]
    #print yloc, xloc
    while (yloc[0] == yloc[1]) and (xloc[0] == xloc[1]):
        yloc, xloc = [np.random.random_integers(0, size_x-1,2), np.random.random_integers(0, size_y-1, 2)]
    map2d[xloc[0]][yloc[0]] = -2
    #print map2d[xloc[0]][yloc[0]]
    map2d[xloc[1]][yloc[1]] = -3
    return map2d

# Generate specific map
def generateMap2d_case1(size_):
# Generates a special map with the middle blocked and passing from left to right being possible at the top or bottom
# part of the map. If for some reason the map fails to generate like that rerun it as it is not foolproof
    size_x, size_y = size_[0], size_[1]
    map2d = generateMap2d(size_)
    map2d[map2d==-2] = 0
    map2d[map2d==-3] = 0
    # add special obstacle
    xtop = [np.random.random_integers(5, 3*size_x//10-2), np.random.random_integers(7*size_x//10+3, size_x-5)]
    ytop = np.random.random_integers(7*size_y//10 + 3, size_y - 5)
    xbot = np.random.random_integers(3, 3*size_x//10-5), np.random.random_integers(7*size_x//10+3, size_x-5)
    ybot = np.random.random_integers(5, size_y//5 - 3)
    map2d[ybot, xbot[0]:xbot[1]+1] = -1
    map2d[ytop, xtop[0]:xtop[1]+1] = -1
    minx = (xbot[0]+xbot[1])//2
    maxx = (xtop[0]+xtop[1])//2
    if minx > maxx:
        tempx = minx
        minx = maxx
        maxx = tempx
    if maxx == minx:
        maxx = maxx+1
    map2d[ybot:ytop, minx:maxx] = -1
    startp = [np.random.random_integers(0, size_x//2 - 4), np.random.random_integers(ybot+1, ytop-1)]
    map2d[startp[1], startp[0]] = -2
    goalp = [np.random.random_integers(size_x//2 + 4, size_x - 3), np.random.random_integers(ybot+1, ytop-1)]
    map2d[goalp[1],goalp[0]] = -3
    return map2d

def plotMap(map2d_, path_):
# Plots a map as described in lab2 description containing integer numbers. Each number has a specific meaning. You can check
# the example provided at the end of the file for more information
    import matplotlib.cm as cm
    greennumber = map2d_.max()
    colors = cm.winter(np.linspace(0, 1, greennumber))
    colorsMap2d = [[[] for x in xrange(map2d_.shape[1])] for y in range(map2d_.shape[0])]
    # Assign RGB Val for starting point and ending point
    # locStart, locEnd = np.where(map2d_ == -2), np.where(map2d_ == -3)
    locStart, locEnd = start,goal
    colorsMap2d[locStart[0]][locStart[1]] = [.0, .0, .0, 1.0]  # black
    colorsMap2d[locEnd[0]][locEnd[1]] = [.0, 1.0, .0, 1.0]  # white
    # # Assign RGB Val for obstacle
    locObstacle = walls
    for iposObstacle in enumerate(locObstacle):
        colorsMap2d[iposObstacle[1][0]][iposObstacle[1][1]] = [1.0, .0, .0, 1.0]
    # # # Assign 0
    locZero = free_cells
    for iposZero in enumerate(locZero):
        colorsMap2d[iposZero[1][0]][iposZero[1][1]] = [1.0, 1.0, 1.0, 1.0]
    # #
    # # # Assign Expanded nodes
    locExpand = expanded_cells
    # #
    for iposExpand in enumerate(locExpand):
        print iposExpand[1][0]
        colorsMap2d[iposExpand[1][0]][iposExpand[1][1]] = colors[map2d_[locExpand[0][iposExpand]][locExpand[1][iposExpand]]-1]
    # #
    list1 = (x[0] for x in path_)
    list2 = (x[1] for x in path_)
    list1, list2 = zip(*path_)
    print list1,list2
    plt.imshow(colorsMap2d, interpolation='nearest')
    plt.plot(list2,list1, color='orange',linewidth=2.5)
    plt.ylim(0,map2d_.shape[0])
    plt.xlim(0,map2d_.shape[1])
    plt.show()

def heuristic(current,goal):
    (x1, y1) = current
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)

def start_to_current(start, current):
    (x1, y1) = start
    (x2, y2) = current
    return abs(x1 - x2) + abs(y1 - y2)

def get_fCost(current):
    return heuristic(current,goal) + start_to_current(start,current)

def get_start_and_goal(target):
    for i, lst in enumerate(mymap):
        for j, color in enumerate(lst):
            if color == -3:
                goal = (i, j)
            if color == -2:
                start = (i, j)
    return start,goal

def unbreachable_walls(map):
    wall = []
    for i, lst in enumerate(mymap):
        for j, color in enumerate(lst):
            if color == -1:
                wall.append((i, j))
    return wall

def no_obstace(map):
    free = []
    for i, lst in enumerate(mymap):
        for j, color in enumerate(lst):
            if color == 0:
                free.append((i, j))
    return free

def get_expanded(map):
    expanded = []
    for i, lst in enumerate(mymap):
        for j, color in enumerate(lst):
            if color > 0:
                expanded.append((i, j))
    return expanded


def passable(id,mymap):
    walls = unbreachable_walls(mymap)
    return id not in walls


def neighbors(id,mymap):
        x, y = id[0],id[1]
        rows = len(mymap)
        col = len(mymap[0])
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse() # aesthetics
        for item in results[:]:
            (a,b) = item
            if a < 0 or a > col or b < 0 or b > rows:
                results.remove(item)
        obs = unbreachable_walls(mymap)
        # print obs
        for item in obs[:]:
            for i in results[:]:
                if i == item:
                    results.remove(i)
        return results

def a_star_search(graph,start,goal):

    frontier = q.PriorityQueue()
    frontier.put(start)

    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        neighbor = neighbors(current,graph)
        for item in neighbor[:]:
            new_cost = cost_so_far[current] + start_to_current(current,item)
            if item not in cost_so_far or new_cost < cost_so_far[item]:
                cost_so_far[item] = new_cost
                priority = new_cost + heuristic(goal, item)
                frontier.put(item)
                came_from[item] = current

    return came_from,cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start) # optional
    path.reverse() # optional
    return path

## Map description
##   0 - Free cell
##   -1 - Obstacle
##   -2 - Start point
##   -3 - Goal point

mymap = generateMap2d_case1([60,60])
# mymap = generateMap2d([20,20]) #This command generates map of the environment
start,goal = get_start_and_goal(mymap) #This command generates start and goal co-ordinates
walls = unbreachable_walls(mymap) #This command gives us the co-ordinates where obstacles are placed
free_cells = no_obstace(mymap)  #This command gives us the co-ordinates where there are free to move
expanded_cells = get_expanded(mymap) #This gives us the map of the environment's which cells are expanded
came,cost=a_star_search(mymap,start,goal) #This function gives us the core functionality of the a* search algorithm
path = reconstruct_path(came, start, goal)
plotMap(mymap,path)
