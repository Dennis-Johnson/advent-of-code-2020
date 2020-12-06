def main():
    with open (r"input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    
    total = 0
    groupAnswers = set()
    
    for i in range(len(lines)):
        line = lines[i]        
        
        # Add the group total when you see a blank line
        if line == "\n" :
            total += len(groupAnswers)
            groupAnswers = set()
            continue
        
        line_set = set(line.rstrip('\n'))

        if len(groupAnswers) == 0 and (i == 0 or lines[i-1] == "\n"):
            groupAnswers = line_set
        else:
            groupAnswers = line_set.intersection(groupAnswers)
        
        # Add to group total if last line in file
        if i == len(lines) - 1:
            total += len(groupAnswers)

    print("Total questions answered: {}".format(total))

if __name__ == "__main__":
    main()
