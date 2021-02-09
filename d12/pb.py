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
            elif grid[i][j] == '#' and getAdjacent(grid, i, j) >= 5:
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
   
    # Top
    for x in reversed(range(0, i)):
        if grid[x][j] == 'L':
            break
        elif grid[x][j] == '#':
            count += 1
            break
    # Bottom 
    for x in range(i+1, r):
        if grid[x][j] == 'L':
                break
        elif grid[x][j] == '#':
            count += 1
            break
    # Left
    for y in reversed(range(0, j)):
        if grid[i][y] == 'L':
            break
        elif grid[i][y] == '#':
            count += 1
            break
    
    # Right
    for y in range(j+1, c):
        if grid[i][y] == 'L':
            break
        elif grid[i][y] == '#':
            count += 1
            break

    #Diag top left
    x = i-1
    y = j-1
    while x >= 0 and y >= 0:
        if grid[x][y] == 'L':
            break
        elif grid[x][y] == '#':
            count += 1
            break
        x -= 1 
        y -= 1
    
    #Diag top right
    x = i - 1
    y = j + 1
    while x >= 0 and y < c:
        if grid[x][y] == 'L':
            break
        elif grid[x][y] == '#':
            count += 1
            break
        x -= 1
        y += 1

    #Diag bottom left
    x = i+1
    y = j-1
    while x < r and y >= 0:
        if grid[x][y] == 'L':
            break
        elif grid[x][y] == '#':
            count += 1
            break
        x += 1 
        y -= 1
    
    #Diag bottom right
    x = i + 1
    y = j + 1
    while x < r and y < c:
        if grid[x][y] == 'L':
            break
        elif grid[x][y] == '#':
            count += 1
            break
        x += 1
        y += 1
 
    return count 

if __name__ == "__main__":
    main()
