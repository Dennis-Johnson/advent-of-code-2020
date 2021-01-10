def main():
    with open(r"input.txt", "r") as inputFile:
        lines = inputFile.readlines()

    maxSeatID = -1

    for line in lines:
        row, col = getRowCol(line[:7], line[-4:])
        seatID = row * 8 + col

        print("SeatID: {}".format(seatID))
        
        if seatID > maxSeatID:
            maxSeatID = seatID
           
    print("The highest SeatID is {}".format(maxSeatID))

def getRowCol(rowSequence, colSequence):
    row = 0
    for i in range(7):
        if rowSequence[i] == 'B':
            row += 2 ** (6 - i)
    
    col = 0
    for i in range(3):
        if colSequence[i] == 'R':
            col += 2 ** (2 - i)
    
    return row, col

if __name__ == "__main__":
    main()
