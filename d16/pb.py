import re
import numpy as np

def isValid(val):
    # Returns true if val is in the range of any field
    for fieldName in fields:
        ranges = fields[fieldName]
        if val >= ranges[0] and val <= ranges[1] or val >= ranges[2] and val <= ranges[3]:
            return True
    return False

def couldBeIn(val):
    # Return possible fields the val could belong to 
    possible = [0] * len(fieldNames)

    for i, fieldName in enumerate(fields):
        ranges = fields[fieldName]
        
        if val >= ranges[0] and val <= ranges[1] or val >= ranges[2] and val <= ranges[3]:
            possible[i] = 1
    
    return possible

fieldLines = open('fieldsTest.txt', 'r').readlines()
#fieldLines = open('fields.txt', 'r').readlines()
fields = {}
fieldNames = []

# Populate the fields dict with field_name: ranges_list[]
for line in fieldLines:
    matchObj = re.findall('(\d+)', line)
    nameObj  = re.search('([^:]*)',line)
    
    if len(matchObj) != 4:
        print("Error: invalid line")
        break
    
    name = nameObj.group()
    fields[name] = [int(x) for x in matchObj]

fieldNames = list(fields.keys())
print(fields)


validTickets = []

ticketLines = open('nearbyTest.txt', 'r').readlines()
#ticketLines = open('nearbyTickets.txt', 'r').readlines()

for line in ticketLines:
    values = line.split(",")
    values = [int(x) for x in values]
    
    for value in values:
        if not isValid(value):
            print("Invalid ticket found {}".format(value))
            break
        
    validTickets.append(values)
            
print(validTickets)


# An iterative solution to find the correct position:
numFields = len(fieldNames)
accumulator = np.zeros((numFields, numFields))

for ticket in validTickets:

    for i, val in enumerate(ticket):
        possible = couldBeIn(val)

        accumulator[i] += possible
    #break
    
print(accumulator)

foundDict = {}
done = False 
while not done:
    num_of_maxes = np.zeros(numFields)
    for k in range(numFields):
        row_max = np.max(accumulator[k])
        max_count = (accumulator[k] == row_max).sum()
        num_of_maxes[k] = max_count

    print(num_of_maxes)
    print(accumulator)
           
    if num_of_maxes.sum() <= numFields:
        # Find row number of largest element left
        i = np.where(accumulator == np.max(accumulator))[0][0]
        done = True

    else:
        i = np.where(num_of_maxes == 1)[0][0]
        j = np.argmax(accumulator[i])
        
        for k in range(numFields):
            accumulator[k][j] = 0

    print("Found field {} at {}".format(fieldNames[j],i))






