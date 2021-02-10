import re

lines = open('test.txt', 'r').readlines()

for line in lines:
    if 'mask' in line:
        mask = line.split()[2]
        print(mask)
    else:
        matchObj = re.search('\[(\d+)\] = (\d+)', line)
        addr, val = matchObj.group(1), matchObj.group(2)
        print(addr, val)

