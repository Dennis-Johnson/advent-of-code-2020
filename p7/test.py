import re 

bags = r"([a-z]+ [a-z]+)"
nums = r"(\d+)"

line1 = "faded blue"
line2 = "bright white 1 shiny gold"
line3 = "vibrant plum 5 faded blue 6 dotted black"

mo1bags = re.search(bags, line1)
mo2bags = re.search(bags, line2)
mo3bags = re.search(bags, line3)

mo1nums = re.search(nums, line1)
mo2nums = re.search(nums, line2)
mo3nums = re.search(nums, line3)

