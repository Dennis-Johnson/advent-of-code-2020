import re

def isValid(val):
    # Returns true if val is in the range of any field
    for field in fields:
        if val >= field[0] and val <= field[1] or val >=field[2] and val <= field[3]:
            return True
    return False


fieldLines = open('fields.txt', 'r').readlines()
fields = []

for line in fieldLines:
    matchObj = re.findall('(\d+)', line)
    
    if len(matchObj) != 4:
        print("Error invalid line")
        break

    fields.append([int(x) for x in matchObj])


print(fields)


errorRate = 0
ticketLines = open('nearbyTickets.txt', 'r').readlines()

for line in ticketLines:
    values = line.split(",")
    values = [int(x) for x in values]
    
    for value in values:
        if not isValid(value):
            print("Invalid value found {}".format(value))
            errorRate += value

print("Error rate: {}".format(errorRate))



