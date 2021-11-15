
def moveship(directions):
    ship = (0,0)
    # headings 'E','N','W','S' = 0,1,2,3
    heading = 0

    for direc in directions:
        if direc[0] == 'N':
            ship = (ship[0]+int(direc[1:]),ship[1])
        if direc[0] == 'S':
            ship = (ship[0]-int(direc[1:]),ship[1])
        if direc[0] == 'E':
            ship = (ship[0],ship[1]+int(direc[1:]))
        if direc[0] == 'W':
            ship = (ship[0],ship[1]-int(direc[1:]))
        if direc[0] == 'L':
            heading = (heading + (int(direc[1:]) // 90)) % 4
        if direc[0] == 'R':
            heading = (heading - (int(direc[1:]) // 90)) % 4
        if direc[0] == 'F':
            if heading == 0:
                ship = (ship[0],ship[1]+int(direc[1:]))
            if heading == 1:
                ship = (ship[0]+int(direc[1:]),ship[1])
            if heading == 2:
                ship = (ship[0],ship[1]-int(direc[1:]))
            if heading == 3:
                ship = (ship[0]-int(direc[1:]),ship[1])

    return(abs(ship[0])+abs(ship[1]))

def movewaypoint(directions):
    point = (1,10)
    ship = (0,0)

    for direc in directions:
        if direc[0] == 'N':
            point = (point[0]+int(direc[1:]),point[1])
        if direc[0] == 'S':
            point = (point[0]-int(direc[1:]),point[1])
        if direc[0] == 'E':
            point = (point[0],point[1]+int(direc[1:]))
        if direc[0] == 'W':
            point = (point[0],point[1]-int(direc[1:]))

        if direc[0] == 'L':
            for _ in range(int(direc[1:]) // 90):
                point = (point[1],-point[0])
        if direc[0] == 'R':
            for _ in range(int(direc[1:]) // 90):
                point = (-point[1],point[0])
        if direc[0] == 'F':
            for _ in range(int(direc[1:])):
                ship = (ship[0]+point[0],ship[1]+point[1])

    return(abs(ship[0])+abs(ship[1]))


def part1(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        print(moveship(lines))

def part2(file):
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
        print(movewaypoint(lines))

def main():
    filename = '../example.txt'
    filename = '../datasets/12.txt'
    part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()
