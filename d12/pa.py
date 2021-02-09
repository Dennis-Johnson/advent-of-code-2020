import math

actions = []
def main():
    for line in open("input.txt").readlines():
        line = line.strip()
        action = line[0]
        amount = int(line[1:])
        actions.append((action, amount))
    print(actions)

    x, y = 0, 0
    heading = 0 #keeping track clockwise
    
    for a in actions:
        act = a[0]
        amt = a[1]

        if act == 'N':
            y += amt
        elif act == 'S':
            y -= amt
        elif act == 'E':
            x += amt
        elif act == 'W':
            x -= amt
        elif act == 'L':
            heading += amt
            if heading > 180: 
                heading = - (360 - heading)
        elif act == 'R':
            heading -= amt
            if heading < -180: 
                heading = 360 - abs(heading)
        elif act == 'F':
            if heading == 0:
                x += amt
            elif heading == 90:
                y += amt
            elif heading == -90:
                y -= amt
            elif abs(heading) == 180:
                x -= amt
        
        print(x, y, heading)

    dist = abs(x) + abs(y)
    print("Manhatten Distance = {}".format(dist))

if __name__ == "__main__":
    main()
