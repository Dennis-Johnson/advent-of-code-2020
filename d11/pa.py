import copy

def main():
    grid = []
    
    #for line in open("test.txt", "r").readlines():
    for line in open("input.txt", "r").readlines():
        grid.append([char for char in line.strip()])

    print(grid) #initial grid
    
    while(True):
        newGrid = nextRound(grid)

        printGrid(newGrid)
        if checkEqual(grid, newGrid):
            print(countOccupied(newGrid))
            break
        else:
            grid = copy.deepcopy(newGrid)

def printGrid(grid):
    for line in grid:
        str = ""
        for seat in line:
            str += seat
        print(str)
    print('\n')

def countOccupied(grid):
    count = 0
    for row in grid:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def nextRound(grid):
    r = len(grid)
    c = len(grid[0])
    newGrid = copy.deepcopy(grid)

    for i in range(r):
        for j in range(c): 
            if grid[i][j] == 'L' and getAdjacent(grid, i,j) == 0 :
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and getAdjacent(grid, i, j) >= 4:
                newGrid[i][j] = 'L'
    return newGrid

def checkEqual(grid, newGrid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != newGrid[i][j]:
                return False
    return True
def getAdjacent(grid, i, j):
    r = len(grid)
    c = len(grid[0])

    count = 0
    
    if (i - 1 >= 0) and grid[i-1][j] == '#':
        count += 1
    if (i + 1 < r ) and grid[i+1][j] == '#':
        count += 1
    if (j - 1 >= 0) and grid[i][j-1] == '#':
        count += 1
    if (j + 1 < c) and grid[i][j+1] == '#':
        count += 1
    if (i - 1 >= 0 and j - 1 >= 0) and grid[i-1][j-1] == '#':
        count += 1
    if (i - 1 >= 0 and j + 1 < c) and grid[i-1][j+1] == '#':
        count += 1
    if (i + 1 < r and j - 1 >= 0) and grid[i+1][j-1] == '#':
        count += 1
    if (i + 1 < r and j + 1 < c) and grid[i+1][j+1] == '#':
        count += 1
    
    return count 

if __name__ == "__main__":
    main()
