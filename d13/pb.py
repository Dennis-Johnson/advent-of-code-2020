from math import ceil

prompt = open('test.txt', 'r').readlines()

buses = [int(id) if id != 'x' else 0 for id in prompt[1].strip().split(',')]
offsets = list(range(0, len(buses)))
indices_to_keep = [i for i in range(len(buses)) if buses[i] != 0]

buses = [buses[i] for i in indices_to_keep]
offsets = [offsets[i] for i in indices_to_keep]

# Sort buses, offsets by decreasing id, but keeping the first bus in place
zipped = list(zip(buses, offsets))
zipped [1:] = sorted(zipped[1:], reverse = True)

# Unzip
buses, offsets = zip(*zipped)
print(buses, offsets)


first_bus = timestamp = buses[0]
largest_other, loff = buses[1], offsets[1]
flag = 0

while(True):
    if (timestamp + loff) % largest_other != 0:
        # Find next closest multiple of first_bus(x) to timestamp + largest (n)
        x = first_bus
        n = timestamp + largest_other
        n = n + x // 2 
        timestamp = n - (n % x)

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


