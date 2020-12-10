nums = []
#for line in open("test.txt", "r").readlines():
for line in open("input.txt", "r").readlines():
    num = line.strip().split()
    nums.append(int(num[0]))

# window= 5
window = 25

for i in range(window, len(nums)):
    lookback = nums[i - window: i]
    valid_sums = set([(x+y) for x in lookback for y in lookback if x != y])

    if nums[i] in valid_sums:
        continue
    else: 
        print("{} is invalid".format(nums[i]))
