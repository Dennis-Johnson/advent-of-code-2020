def main():
    with open(r"input.txt", "r") as inputFile:
        lines = inputFile.readlines()

    maxSeatID = -1
    minSeatID = 1000000000
    total = 0
    for line in lines:
        row, col = getRowCol(line[:7], line[-4:])
        seatID = row * 8 + col
        
        total += seatID
        print("SeatID: {}".format(seatID))
        
        if seatID > maxSeatID:
            maxSeatID = seatID
        if seatID < minSeatID:
            minSeatID = seatID

    print("Max, Min SeatIDs are {}, {}".format(maxSeatID, minSeatID))
    
    expectedSum = (maxSeatID * (maxSeatID + 1) / 2) - (minSeatID * (minSeatID - 1) / 2)
    missing = expectedSum - total
    
    print("Your seat is {}".format(missing))


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
