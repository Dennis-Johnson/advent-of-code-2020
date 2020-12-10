nums = []
#for line in open("test.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    num = line.strip().split()
    nums.append(int(num[0]))

#window= 5
window = 25

for i in range(window, len(nums)):
    lookback = nums[i - window: i]
    valid_sums = set([(x+y) for x in lookback for y in lookback if x != y])

    if nums[i] in valid_sums:
        continue
    else: 
        invalid = nums[i]
        print("{} is invalid".format(nums[i]))

for low in range(len(nums)):
    for high in range(low + 1, len(nums)):
        if low == high: 
            continue

        c_sum = sum(nums[low: high])
        
        if c_sum == invalid:
            smallest, largest = min(nums[low:high]), max(nums[low:high])
            print("Min + Max = {} + {} = {}".format(smallest, largest, smallest + largest))
        
        elif c_sum > invalid:
            break
