import re

def main():
    with open(r"input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()    

    validCount = 0
    

    details = ""
    for i in range(len(lines)):
        line = lines[i]
        
        # If last line in file
        if i == len(lines) - 1:
            details += line.rstrip('\n')

        # End of current passport or end of file
        if line == "\n" or i == len(lines) - 1 :
            # Remove trailing space and verify fields
            if verify(details.strip()) :
                validCount += 1
            details = ""

        else:
            details += line.rstrip('\n') + ' '

    print("Valid Passports: {}".format(validCount))

# Returns true if details are valid
def verify(details):
    patterns = ["byr:([0-9]{4})($|\s)",
                "iyr:([0-9]{4})($|\s)",
                "eyr:([0-9]{4})($|\s)",
                "hgt:([0-9]+)(cm|in)($|\s)",
                "hcl:#[0-9a-f]{6}($|\s)",
                "ecl:(amb|blu|brn|gry|grn|hzl|oth)($|\s)",
                "pid:([0-9]{9})($|\s)"]
    
    validFields = 0
    cidFound = False
    
    # Check each pattern for match and add to tally
    for i in range(len(patterns)):
        pattern = r"{}".format(patterns[i])
        matchObj = re.search(pattern, details, re.I)
        
        if matchObj:
            if i == 0:  #byr
                year = int(matchObj.group(1))
                if year > 2002 or year < 1920:
                    continue
            
            elif i == 1:    #iyr
                year = int(matchObj.group(1))
                if year > 2020 or year < 2010:
                    continue
            
            elif i == 2:     #eyr
                year = int(matchObj.group(1))
                if year > 2030 or year < 2020:
                    continue

            elif i == 3:    #hgt
                height = int(matchObj.group(1))
                unit = matchObj.group(2)

                if unit == "cm":
                    if height > 193 or height < 150:
                        continue
                elif unit == "in":
                    if height > 76 or height < 59:
                        continue

            # the other fields (hcl, ecl, pid) are validated with the regexp itself
            validFields += 1
    
    print(validFields)

    #cidFound is not used 
    if re.search(r"cid:", details):
        cidFound = True
    
    if validFields == 7: 
        return True

    return False

if __name__ == "__main__":
    main()
