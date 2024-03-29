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

timestamp = offsets[0]
i = 0
step = buses[0]

while(True):
    if i >= len(buses)-1:
        break

    if (timestamp + offsets[i+1]) % buses[i+1] == 0:
        step *= buses[i+1]
        #step = compute_lcm(buses[i], step)
        i += 1
    else:
        timestamp += step

print('TS: {}'.format(timestamp))

