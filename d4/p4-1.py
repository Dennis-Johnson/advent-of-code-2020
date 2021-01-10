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
    patterns = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
    
    validFields = 0
    cidFound = False
    
    # Check each pattern for match and add to tally
    for pattern in patterns:
        if re.search(pattern, details):
            validFields += 1
   
    #cidFound is not used 
    if re.search(r"cid:", details):
        cidFound = True
    
    if validFields == 7: 
        return True

    return False

if __name__ == "__main__":
    main()
