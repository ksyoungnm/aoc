

import os

def get_neighbors(tn, grid):
    to_visit = []
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        if (0 <= tn[0] + dx < len(grid)) and (0 <= tn[1] + dy < len(grid[0])):
            to_visit.append((tn[0] + dx, tn[1] + dy))
    return to_visit


def count_trailheads(grid):
    total_mountains = 0
    for row_i in range(len(grid)):
        for col_j in range(len(grid[0])):
            if grid[row_i][col_j] == "0":
                visited = set()
                queue = [(row_i, col_j)]

                while len(queue) > 0:
                    tn = queue.pop()
                    neighbors = get_neighbors(tn, grid)
                    for n in neighbors:
                        if int(grid[n[0]][n[1]]) == int(grid[tn[0]][tn[1]]) + 1:
                            if int(grid[n[0]][n[1]]) == 9: visited.add(n)
                            else: queue.append(n)

                total_mountains += len(visited)
    return total_mountains

def count_trailheads2(grid):
    total_mountains = 0
    for row_i in range(len(grid)):
        for col_j in range(len(grid[0])):
            if grid[row_i][col_j] == "0":
                visited = dict()
                queue = [(row_i, col_j, 1)]

                while len(queue) > 0:
                    tn = queue.pop()
                    neighbors = get_neighbors(tn, grid)
                    for n in neighbors:
                        if int(grid[n[0]][n[1]]) == int(grid[tn[0]][tn[1]]) + 1:
                            if int(grid[n[0]][n[1]]) == int(grid[tn[0]][tn[1]]) + 1:
                                if int(grid[n[0]][n[1]]) == 9:
                                    if n in visited: visited[n] += 1
                                    else: visited[n] = 1
                                else: queue.append(n)


                total_mountains += sum(visited.values())
    return total_mountains


def part1(filename):

    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        print(count_trailheads(grid))


def part2(filename):

    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        print(count_trailheads2(grid))

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
