def main():
    with open (r"input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    
    total = 0
    questions = set()
    
    for i in range(len(lines)):
        line = lines[i]        

        # Add the group total when you see a blank line
        if line == "\n" :
            total += len(questions)
            questions = set()
            continue

        for char in line.rstrip('\n'):
            questions.add(char)
        
        # Add to group total if last line in file
        if i == len(lines) - 1:
            total += len(questions)

    print("Total questions answered: {}".format(total))

if __name__ == "__main__":
    main()
