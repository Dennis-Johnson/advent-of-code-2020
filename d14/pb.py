import re
from itertools import combinations

def parse_mask(inpString):
    inpString = inpString[::-1]
    # list of indices of 0,1,or X in the mask string
    zeros = [i for i, letter in enumerate(inpString) if letter == '0']
    ones  = [i for i, letter in enumerate(inpString) if letter == '1'] 
    exes  = [i for i, letter in enumerate(inpString) if letter == 'X']
    return zeros, ones, exes

def set_bits(num, ones, zeros):
    for pos in ones:
        num |=  (1 << pos)
    for pos in zeros:
        num &= ~(1 << pos)
    return num

def get_addresses(addr, mask):
    zeros, ones, exes = parse_mask(mask)

    # representation of resulting mask before permuting the X positions
    # e.g --> addr = 42 = 101010, mask = X1001X
    # itermediate = 010010 | 101010 = 111010
    intermediate = set_bits(0, ones, zeros) | addr

    print(bin(addr), bin(intermediate))
    new_addresses = []

    for i in range(0, len(exes) + 1):
        # combs contains list of tuples with possible combinations of length i 
        combs  = list(combinations(exes, i))  
        
        for comb in combs:
            new_ones  = list(comb)
            new_zeros = [i for i in exes if i not in new_ones]

            new_addr = set_bits(intermediate, new_ones, new_zeros)
            new_addresses.append(new_addr)

    return new_addresses

lines = open('input.txt', 'r').readlines()
memory = {}

for line in lines:
    if 'mask' in line:
        mask = line.split()[2]
    else:
        matchObj = re.search('\[(\d+)\] = (\d+)', line)
        addr, val = int(matchObj.group(1)), int(matchObj.group(2))
        new_addrs = get_addresses(addr, mask)

        for new_addr in new_addrs:
            print("Write {} to new_addr {}".format(val, new_addr))
            memory[new_addr] = val
        
print("Sum @ all memory values = {}".format(sum(memory.values())))
        


