"""Implement a* algorithm for any game search algorithm!"""

import numpy as np

class Node:
def __init__(self, parent=None, position=None):
self.parent = parent # parent of current node
self.position = position # current position

self.g = 0 # cost from start to end
self.h = 0 # estimated cost from current to end
self.f = 0 # total cost f = g + h

def __eq__(self, other):
return self.position == other.position

def ReturnPath(currentNode, maze):
path = []
noRows, noColumns = np.shape(maze)

# create result maze with -1 in every position
result = [[-1 for i in range(noColumns)] for j in range(noRows)]
current = currentNode

while current is not None:
path.append(current.position)
current = current.parent
# Return reversed path 
path = path[::-1]
startValue = 0
# update path of start to end incremented by 1
for i in range(len(path)):
result[path[i][0]][path[i][1]] = startValue
startValue += 1
return result

def Search(maze, cost, start, end):
startNode = Node(None, tuple(start))
startNode.g = startNode.h = startNode.f = 0
endNode = Node(None, tuple(end))
endNode.g = endNode.h = endNode.f = 0

# lowest cost node to expand next
yetToVisitList = []
# already explored, don't explore again
visitedList = []

# Add start node
yetToVisitList.append(startNode)

# stop condition avoid any infinite loop execution after some number of steps
outerIterations = 0
maxIterations = (len(maze) // 2) ** 10

# search movement is left-right-top-bottom
move = [[-1, 0], # go up
[0, -1], # go left
[1, 0], # go down
[0, 1]] # go right

noRows, noColumns = np.shape(maze)

while len(yetToVisitList) > 0:
# any node referred from yettovisitlist then counter of limit operation incremented
outerIterations += 1

# Get current node
currentNode = yetToVisitList[0]
currentIndex = 0
for index, item in enumerate(yetToVisitList):
if item.f < currentNode.f:
currentNode = item
currentIndex = index

# if we hit this point return path as there may be no solution or cost too high
if outerIterations > maxIterations:
print("Path not feasible!")
return ReturnPath(currentNode, maze)

# Pop current node out of yettovisitlist, add to visited list
yetToVisitList.pop(currentIndex)
visitedList.append(currentNode)

# test if goal is reached or not, if yes then return the path
if currentNode == endNode:
return ReturnPath(currentNode, maze)

# Generate children from all adjacent squares
children = []

for newPosition in move:
# Get node position
nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

# Make sure within maze boundary
if (nodePosition[0] > (noRows - 1) or nodePosition[0] < 0 or nodePosition[1] > (noColumns - 1) 
or nodePosition[1] < 0):
continue

if maze[nodePosition[0]][nodePosition[1]] != 0:
continue

newNode = Node(currentNode, nodePosition)

children.append(newNode)

# Loop through children
for child in children:
# Child is on the visited list then skip
if len([visitedChild for visitedChild in visitedList if visitedChild == child]) > 0:
continue

# Create the f, g, and h values
child.g = currentNode.g + cost

# Heuristic costs calculated here
child.h = (((child.position[0] - endNode.position[0]) ** 2) +
((child.position[1] - endNode.position[1]) ** 2))

child.f = child.g + child.h

# Child is already in the yettovisitlist and g cost is already lower
if len([i for i in yetToVisitList if child == i and child.g > i.g]) > 0:
continue

# Add the child to the yettovisitlist
yetToVisitList.append(child)

if __name__ == '__main__':
# 1 represents wall
maze = [[0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1]]

start = [0, 0] # starting position
end = [3, 3] # ending position
cost = 2 # cost per movement

path = Search(maze, cost, start, end)
print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row])
for row in path]))

