import re

def main():
    validCount = 0

    with open('input.txt', 'r') as inpFile:
        lines = inpFile.readlines()

        for line in lines:
            matchObj = re.findall(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)', line, re.I)[0]
            lowerIndex = int(matchObj[0])
            upperIndex = int(matchObj[1])
            letter = matchObj[2]
            string = matchObj[3]
            
            
            lowerValid = string[lowerIndex - 1] == letter
            upperValid = string[upperIndex - 1] == letter

            if lowerValid ^ upperValid:
                validCount += 1

    print("There are {} valid passwords".format(validCount))

if __name__ == "__main__":
    main()
