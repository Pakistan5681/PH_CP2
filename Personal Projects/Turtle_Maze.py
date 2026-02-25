import turtle as t
from random import choice

gridSize = 5
gridRows = []
gridCollumns = []
spaceSize = 80

t.tracer(0, 0)
t.speed(1000)

def randomList(gridSize):
    outList = []
    options = ["open", "closed"]

    for i in range(gridSize):
        outList.append(choice(options))

    return outList

for x in range(gridSize):
    gridRows.append(randomList(gridSize))
    gridCollumns.append(randomList(gridSize))

def moveDrawing(size, gridSize):
    canvas = t.getcanvas()

    for element_id in canvas.find_all():
        canvas.move(element_id, (size * gridSize) / -2, (size * gridSize) / 2)

def drawLineHorizontal(x, y, distance):
    t.teleport(x, y)
    t.forward(distance)

def drawLineVertical(x, y, distance):
    t.teleport(x, y)
    t.forward(distance)

def drawLineVerticalEdgeCase(x, y, distance, rotation):
    t.teleport(x, y)
    t.left(rotation)
    t.forward(distance)
    t.right(rotation)

def drawMaze(rows, collumns, spaceSize, gridSize):
    drawLineHorizontal(0, 0, spaceSize * gridSize)
    drawLineHorizontal(0, (spaceSize * gridSize), spaceSize * gridSize)
    drawLineVerticalEdgeCase(spaceSize * gridSize, 0, (spaceSize * (gridSize - 1)), 90)
    drawLineVerticalEdgeCase(0, spaceSize * gridSize, (spaceSize * (gridSize - 1)), 270)

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == "open":
                t.penup()
            else:
                t.pendown()

            drawLineHorizontal(j * spaceSize, i * spaceSize, spaceSize)

    t.left(90)
    for i in range(len(collumns)):
        for j in range(len(collumns[i])):
            if i != 0 and i != gridSize:
                if collumns[i][j] == "open":
                    t.penup()
                else:
                    t.pendown()
            else:
                t.penup()

            
            drawLineVertical(i * spaceSize, j * spaceSize, spaceSize)

    t.left(90)

def checkSolvable(rows, collumns, size, gridCount):
    mazeCheckers = [[0, 0]]
    visitedSpaces = []

    solvable = False

    while bool(mazeCheckers):
        for i in mazeCheckers:

            if i == [gridSize - 1, gridSize - 1]:
                solvable = True
                print("Solved")
                return True

            if (i[1] + 1) * size < size * gridCount and (i[0]) * size < size * gridCount:
                if rows[i[1] + 1][i[0]] == "open" and not [i[0], i[1] + 1] in visitedSpaces: # checks if no line above
                    mazeCheckers.append([i[0], i[1] + 1])
                    visitedSpaces.append([i[0], i[1]])

            if ((i[1]) * size > size * gridCount):
                if rows[i[1]][i[0]] == "open" and (i[1] - 1) * size > 0 and not [i[0], i[1] - 1] in visitedSpaces: # checks if no line below
                    mazeCheckers.append([i[0], i[1] - 1])
                    visitedSpaces.append([i[0], i[1]])

            if (i[1]) * size < size * gridCount and (i[0] + 1) * size < size * gridCount:
                if collumns[i[0] + 1][i[1]] == "open" and not [i[0] + 1, i[1]] in visitedSpaces: # checks if no line to right
                    mazeCheckers.append([i[0] + 1, i[1]])
                    visitedSpaces.append([i[0], i[1]])

            if collumns[i[0]][i[1]] == "open" and (i[0] - 1) * size > 0 and not [i[0] - 1, i[1]] in visitedSpaces: # checks if no line to left
                mazeCheckers.append([i[0] - 1, i[1]])
                visitedSpaces.append([i[0], i[1]])

            mazeCheckers.remove(i)  

    return solvable

gridSizeInput = input("How big do you want the grid to be? \nMake it four or above so it doesn't break: ")

while not gridSizeInput.isnumeric():
    gridSizeInput = input("How big do you want the grid to be? ")

gridSize = int(gridSizeInput)

mazeSize = "" 

while not mazeSize.isnumeric():
    mazeSize = input("How big do you want the enitire maze to be? \nKeep it at 1300 or less to keep it on screen: ")

mazeSize = int(mazeSize)

spaceSize = mazeSize / gridSize

for x in range(0, gridSize):      
        gridRows.append(randomList(gridSize))
        gridCollumns.append(randomList(gridSize))

print("Generating Maze")

if(gridSize >= 50):
    print("This may take a while")
            
while checkSolvable(gridRows, gridCollumns, spaceSize, gridSize) == False:
    gridRows = []
    gridCollumns = []
    for x in range(0, gridSize):      
        gridRows.append(randomList(gridSize))
        gridCollumns.append(randomList(gridSize))
    
drawMaze(gridRows, gridCollumns, spaceSize, gridSize)

t.update()
moveDrawing(spaceSize, gridSize)
t.mainloop()