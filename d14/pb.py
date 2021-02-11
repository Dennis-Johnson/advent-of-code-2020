import re

def parse_mask(inpString):
    inpString = inpString[::-1]
    ones  = [i for i, letter in enumerate(inpString) if letter == '1'] 
    zeros = [i for i, letter in enumerate(inpString) if letter == '0']
    return ones, zeros

def apply_mask(num, ones, zeros):
    for pos in ones:
        num |=  (1 << pos)
    for pos in zeros:
        num &= ~(1 << pos)

    return num

lines = open('input.txt', 'r').readlines()
memory = {}

for line in lines:
    if 'mask' in line:
        ones, zeros = parse_mask(line.split()[2])
    else:
        matchObj = re.search('\[(\d+)\] = (\d+)', line)
        addr, val = matchObj.group(1), int(matchObj.group(2))

        val = apply_mask(val, ones, zeros)
        memory[addr] = val

print("Sum @ all memory values = {}".format(sum(memory.values())))
        


