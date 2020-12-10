adapters = [0]

#for line in open("test.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    adapter = line.strip().split()
    adapters.append(int(adapter[0]))

adapters.append(max(adapters) + 3)
adapters.sort()

diffs = []
for i in range(1, len(adapters)):
    diffs.append(adapters[i] - adapters[i-1])

print(diffs)

ones, threes = diffs.count(1), diffs.count(3)
print("Product of 1 and 3 diffs = {}".format(ones * threes))
