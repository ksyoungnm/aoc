

import os



def part1(filename):

    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        total = 0
        for row_i in range(len(lines)):
            for col_j in range(len(lines[row_i])):
                # if lines[row_i][col_j] == 'X':

                # right
                if lines[row_i][col_j:col_j + 4] == "XMAS":
                    # print(f"found {row_i},{col_j}")
                    total += 1

                # right-down
                if row_i + 3 < len(lines) and col_j + 3 < len(lines[row_i]):
                    if lines[row_i][col_j] + lines[row_i+1][col_j+1] + lines[row_i+2][col_j+2] + lines[row_i+3][col_j+3] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # down
                if row_i + 3 < len(lines):
                    if lines[row_i][col_j] + lines[row_i+1][col_j] + lines[row_i+2][col_j] + lines[row_i+3][col_j] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # down-left
                if row_i + 3 < len(lines) and col_j >= 3:
                    if lines[row_i][col_j] + lines[row_i+1][col_j-1] + lines[row_i+2][col_j-2] + lines[row_i+3][col_j-3] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # left
                if col_j >= 3:
                    if lines[row_i][col_j - 3:col_j+1] == "SAMX":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # left-up
                if row_i >= 3 and col_j >= 3:
                    if lines[row_i][col_j] + lines[row_i-1][col_j-1] + lines[row_i-2][col_j-2] + lines[row_i-3][col_j-3] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # up
                if row_i >= 3:
                    if lines[row_i][col_j] + lines[row_i-1][col_j] + lines[row_i-2][col_j] + lines[row_i-3][col_j] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # up-right
                if row_i >= 3 and col_j + 3 < len(lines[row_i]):
                    if lines[row_i][col_j] + lines[row_i-1][col_j+1] + lines[row_i-2][col_j+2] + lines[row_i-3][col_j+3] == "XMAS":
                        # print(f"found {row_i},{col_j}")
                        total += 1

                # if row_i == 4 and col_j == 0:
                #     print(lines[row_i][col_j] + lines[row_i-1][col_j] + lines[row_i-2][col_j] + lines[row_i-3][col_j])
        print(total)



def part2(filename):

    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        total = 0
        for row_i in range(1, len(lines)-1):
            for col_j in range(1, len(lines[row_i])-1):
                diag_1 = lines[row_i-1][col_j-1] + lines[row_i][col_j] + lines[row_i+1][col_j+1]
                diag_2 = lines[row_i-1][col_j+1] + lines[row_i][col_j] + lines[row_i+1][col_j-1]
                if (diag_1 == "MAS" or diag_1 == "SAM") and (diag_2 == "MAS" or diag_2 == "SAM"):
                    total+=1
        print(total)



def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
