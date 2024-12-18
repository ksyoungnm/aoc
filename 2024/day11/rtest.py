

import os



def part1(filename):

    with open(filename) as f:
        stones = f.readline().split()
        for j in range(25):
            i = 0
            while i < len(stones):
                # print(len(stones[i]) % 2 == 0)
                # i += 1
                if len(stones[i]) % 2 == 0:
                    half_1 = stones[i][:len(stones[i])//2]
                    half_2 = str(int(stones[i][len(stones[i])//2:]))
                    stones = stones[:i] + [half_1, half_2] + stones[i+1:]
                    i += 2
                    # i += 1
                else:
                    if stones[i] == "0": stones[i] = "1"
                    else: stones[i] = str(int(stones[i]) * 2024)
                    i += 1
            print(j, len(stones))


        print(len(stones))



def process_val(value):
    if value == "0":
        return ["1"]
    elif len(value) % 2 == 0:
        return [value[:len(value)//2], str(int(value[len(value)//2:]))]
    else:
        return [str(int(value) * 2024)]



def part2(filename):

    with open(filename) as f:
        stones = f.readline().split()
        links = {}
        pointers = {s:1 for s in stones}

        for _ in range(75):

            next_pointers = {}

            for p in pointers:
                if p not in links:
                    links[p] = process_val(p)

                for np in links[p]:
                    if np not in next_pointers:
                        next_pointers[np] = 0
                    next_pointers[np] += pointers[p]

            pointers = next_pointers

        print(sum(pointers.values()))







def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
