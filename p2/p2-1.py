import re

def main():
    validCount = 0

    with open('input.txt', 'r') as inpFile:
        lines = inpFile.readlines()

        for line in lines:
            matchObj = re.findall(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)', line, re.I)[0]
            lowerBound = int(matchObj[0])
            upperBound = int(matchObj[1])
            letter = matchObj[2]
            string = matchObj[3]
            
            letterCount = 0
            for char in string:
                if char == letter:
                    letterCount += 1

            if letterCount >= lowerBound and letterCount <= upperBound:
                validCount += 1
    
    print("There are {} valid passwords".format(validCount))

if __name__ == "__main__":
    main()
