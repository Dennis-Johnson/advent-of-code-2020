from math import sin, cos, pi

actions = []
def main():
    #for line in open("test.txt").readlines():
    for line in open("input.txt").readlines():
        line = line.strip()
        action = line[0]
        amount = int(line[1:])
        actions.append((action, amount))
    print(actions)

    x, y = 0, 0
    wx, wy = 10, 1

    for act, amt in actions:
        if act == 'N':
            wy += amt
        elif act == 'S':
            wy -= amt
        elif act == 'E':
            wx += amt
        elif act == 'W':
            wx -= amt
        elif act == 'F':
            x += wx * amt
            y += wy * amt
        else:
            if act == 'R':
                amt *= -1 
            wx, wy = update_waypoint(amt, wx, wy)

        print(x, y, wx, wy)

    print("Manhatten Distance = {}".format(abs(x) + abs(y)))

def update_waypoint(amt, wx, wy):
    
    if amt == 270:
        amt = -90
    elif amt == -270: 
        amt = 90

    if amt == 90:
        wx, wy = -wy, wx
    elif amt == -90:
        wx, wy = wy, -wx
    elif abs(amt) == 180:
        wx, wy = -wx, -wy

    return wx, wy

if __name__ == "__main__":
    main()
