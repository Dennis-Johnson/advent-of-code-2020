import time

def main(adapters):
    #for line in open("input.txt", "r").readlines():
    for line in open("test2.txt", "r").readlines():
        adapter = line.strip().split()
        adapters.append(int(adapter[0]))

    adapters.append(max(adapters) + 3)
    adapters.sort()
    
    '''
    diffs = []
    for i in range(1, len(adapters)):
        diffs.append(adapters[i] - adapters[i-1])
    '''
    # test = [0, 1, 2, 3, 5, 6]
    ways = check(adapters)
    print(ways)

def check(adapters):
    # Only port and device left in list
    if len(adapters) <= 2 or not isValid(adapters):
        return 0
    else: 
        ways = 1 
    
    print(adapters)
    # Don't touch the first and last element
    
    temp = adapters[1: len(adapters) - 1]
    for i in temp:
        # Check combos where one of the middle adapters are taken out
        ways += check([adapters[0]] + [x for x in temp if x != i] + [adapters[-1]])
    return ways

def bottom_up():
    pass

def isValid(adapters):
    for i in range(1, len(adapters)):
        if 3 < (adapters[i] - adapters[i-1]) < 1:
            return False

    return True


if __name__ == "__main__":
    adapters = [0]
    main(adapters)
