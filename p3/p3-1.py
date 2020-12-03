import numpy as np

def main():
    
    # Hard coding dimensions of the terrain map from the puzzle input
    input_dims = (323, 31)
    terrain = np.zeros(input_dims)

    with open(r"input.txt", "r") as inpFile:
        lines = inpFile.readlines()
        
    # Convert each line into a logical array
    # 1 -> tree '#' and 0 -> no tree '.'    
    for i in range(len(lines)):

        #Loop over chars in the line to form row of terrain
        for j in range(input_dims[1]):
            terrain[i][j] = lines[i][j] == '#'

    xpos, ypos = 0, 0
    treeCount = 0

    while ypos < input_dims[0]:
        if terrain[ypos][xpos] == 1:
            treeCount += 1

        xpos = (xpos + 3) % input_dims[1]
        ypos += 1

    print("Encountered {} trees".format(treeCount))


if __name__ == "__main__":
    main()
