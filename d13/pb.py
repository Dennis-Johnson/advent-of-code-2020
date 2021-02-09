from math import ceil

prompt = open('input.txt', 'r').readlines()

buses = [int(id) if id != 'x' else 0 for id in prompt[1].strip().split(',')]
offsets = list(range(0, len(buses)))
indices_to_keep = [i for i in range(len(buses)) if buses[i] != 0]

buses = [buses[i] for i in indices_to_keep]
offsets = [offsets[i] for i in indices_to_keep]
print(buses, offsets)

first_bus = timestamp = buses[0]
flag = 0

while(True):
    flag = 0
    for i in range(1, len(buses)):
        if (timestamp + offsets[i]) % buses[i] != 0:
            flag = 1
            break
    
    if flag == 1:
        timestamp += first_bus
    else:
        break

print(timestamp)


