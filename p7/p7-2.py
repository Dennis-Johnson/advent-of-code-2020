import re

'''
Do the following transformations to the input:
1.Remove commas and periods
2.Remove [bag, bags, contain]
3.Remove 'no other'
'''
def main():
    with open ("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    
    # Bag matches each bag of form (adjective color)
    # The first match is the outermost bag
    bag = r"([a-z]+ [a-z]+)"

    # Correlate number of bags to each bag name (except the first one)

    num = r"(\d+)"
    
    # Dict of all bags
    bags = {}
    for line in lines:
        names = re.findall(bag, line)
        nums  = re.findall(num, line)
        
        outer = names[0]

        #Exclude the first name from contents
        contents = dict(zip(names[1:], nums))
        
        bags[outer] = contents
    
    hit = "shiny gold"
    count = explore(bags, hit)
    # The graph search will count an extra path of shiny gold to itself
    print(count)

def explore (graph, start):
    if not graph[start]:
        return 1
    
    count = 1
    for node in graph[start]:
        num = int(graph[start][node])    
        print(start, node, num)
        count += explore(graph, node) * num

    return count

def find_path(graph, start, end, path=[]):
    path = path + [start]
    global count
    if start == end:
        count += 1
        return path
    
    if not start in graph.keys():
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

if __name__ == "__main__":
    main()
