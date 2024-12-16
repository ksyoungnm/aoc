
import os

def walk(start, direction, grid):
    ch_i, ch_j = start
    path = [(ch_i, ch_j, direction)]

    while True:

        # set up which position to check next
        tc_i, tc_j = -1, -1
        if direction == 0: tc_i, tc_j = ch_i - 1, ch_j
        if direction == 1: tc_i, tc_j = ch_i, ch_j + 1
        if direction == 2: tc_i, tc_j = ch_i + 1, ch_j
        if direction == 3: tc_i, tc_j = ch_i, ch_j - 1

        # if we've left the grid, then we're done, and arent looping.
        if (tc_i < 0 or tc_i >= len(grid)) or (tc_j < 0 or tc_j >= len(grid[0])):
            return path, None

        # otherwise, we need to check if tc_ is a hash. if it is, we need to
        # rotate until we're pointing to an open spot. i believe its impossible
        # to rotate to a position outside the grid, but not 100% sure
        while grid[tc_i][tc_j] == "#":
            direction = (direction + 1) % 4
            if direction == 0: tc_i, tc_j = ch_i - 1, ch_j
            if direction == 1: tc_i, tc_j = ch_i, ch_j + 1
            if direction == 2: tc_i, tc_j = ch_i + 1, ch_j
            if direction == 3: tc_i, tc_j = ch_i, ch_j - 1

        # then, we step forward
        ch_i, ch_j = tc_i, tc_j
        path.append((ch_i, ch_j, direction))

        # if we have already been at this place, facing this direction,
        # we are in a loop
        loop_index = path.index((ch_i, ch_j, direction))
        if loop_index < len(path) - 1:
            return path, loop_index

def meta_walk(start, direction, grid):
    # ok, same idea, walk the path, each time we check a spot, before we move
    # we're gonna test if it would bring us into a loop.
    ch_i, ch_j = start

    # important to not check spots we've already checked. this prevents 1.
    # double counting and 2. if we run into the same spot later from a
    # different direction that does produce a loop, we still dont want to count it.
    visited = {start: False}
    i = 0

    while True:
        # just to watch progress
        if i % 100 == 0:
            print(i)

        # set up the position to check next
        tc_i, tc_j = -1, -1
        if direction == 0: tc_i, tc_j = ch_i - 1, ch_j
        if direction == 1: tc_i, tc_j = ch_i, ch_j + 1
        if direction == 2: tc_i, tc_j = ch_i + 1, ch_j
        if direction == 3: tc_i, tc_j = ch_i, ch_j - 1

        # if we've left the grid, then we're done!.
        if (tc_i < 0 or tc_i >= len(grid)) or (tc_j < 0 or tc_j >= len(grid[0])):
            return visited

        # otherwise, we need to check if tc_ is a hash. if it is, we need to
        # rotate until we're pointing to an open spot. i believe its impossible
        # to rotate to a position outside the grid, but not 100% sure
        while grid[tc_i][tc_j] == "#":
            direction = (direction + 1) % 4
            if direction == 0: tc_i, tc_j = ch_i - 1, ch_j
            if direction == 1: tc_i, tc_j = ch_i, ch_j + 1
            if direction == 2: tc_i, tc_j = ch_i + 1, ch_j
            if direction == 3: tc_i, tc_j = ch_i, ch_j - 1

        # if we've already checked this spot, don't need to again.
        if (tc_i, tc_j) not in visited:

            # now, we pretend theres a blockage at tc. pass the fake
            # grid to walk and see if that produces a loop
            grid[tc_i] = grid[tc_i][:tc_j] + "#" + grid[tc_i][tc_j+1:]
            path, loop_idx = walk((ch_i, ch_j), direction, grid)
            visited[(tc_i, tc_j)] = loop_idx is not None
            grid[tc_i] = grid[tc_i][:tc_j] + "." + grid[tc_i][tc_j+1:]

        # then, we step forward
        ch_i, ch_j = tc_i, tc_j
        i += 1


def part1(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        ch_i, ch_j = -1, -1
        for ch_i,line in enumerate(grid):
            try: ch_j = line.index("^"); break;
            except ValueError: continue
        grid[ch_i] = grid[ch_i][:ch_j] + "." + grid[ch_i][ch_j+1:]

        start = (ch_i, ch_j)
        direction = 0
        path, looping = walk(start, direction, grid)
        unique = set((pi,pj) for pi,pj,di in path)
        print(len(unique))


def part2(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
        ch_i, ch_j = -1, -1
        for ch_i,line in enumerate(grid):
            try: ch_j = line.index("^"); break;
            except ValueError: continue
        grid[ch_i] = grid[ch_i][:ch_j] + "." + grid[ch_i][ch_j+1:]

        start = (ch_i, ch_j)
        direction = 0
        visited = meta_walk(start, direction, grid)
        print(len([block for block in visited if visited[block]]))



def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
