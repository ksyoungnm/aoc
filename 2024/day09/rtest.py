

import os

def gen_harddisk(disk):
    file = True
    file_index = 0
    disk_list = []
    for ch in disk:
        for _ in range(int(ch)):
            if file: disk_list.append(file_index)
            else: disk_list.append(None)
        if file:
            file_index += 1
        file = not file
    return disk_list

def last_nonNone(list, guess):
    while list[guess] is None:
        guess -= 1
    return guess

def compress(disk):
    end_idx = last_nonNone(disk, len(disk) - 1)
    i = 0
    while i < end_idx:
        if disk[i] is None:
            disk[i] = disk[end_idx]
            disk[end_idx] = None
            end_idx = last_nonNone(disk, end_idx)
        i += 1
    return disk

class diskNode:
    def __init__(self, start_pos, length, filetype, next = None, prev = None):
        self.start_pos = start_pos
        self.length = length
        self.filetype = filetype
        self.prev = prev
        self.next = next
        self.moved = False

# def gen_disk2(disk):


def compress2(disk):
    moved = set()

    for bc_i in range(len(disk)-1, -1, -1):

        if disk[bc_i] is not None:
            if disk[bc_i] not in moved:

                filesize = 0
                while disk[bc_i - filesize] ==  disk[bc_i]:
                    filesize += 1

                gap_idx = 0
                gap_size = 0
                while gap_size < filesize:
                    if gap_idx >= bc_i:
                        gap_idx, gap_size = -1, -1
                        break
                    if disk[gap_idx + gap_size] == None:
                        gap_size += 1
                    else:
                        gap_idx += 1
                        gap_size = 0

                if gap_idx != -1:
                    for i in range(gap_idx, gap_idx + gap_size):
                        disk[i] = disk[bc_i]
                    for i in range(bc_i - filesize + 1, bc_i + 1):
                        disk[i] = None


                # print(disk)
                moved.add(disk[bc_i])
    return disk



def calc_checksum(disk):
    total = 0
    for i,item in enumerate(disk):
        if item is not None:
            total += i * item
    return total

def part1(filename):

    with open(filename) as f:
        disk = f.readline().strip()
        disk = gen_harddisk(disk)
        disk = compress(disk)
        disk = calc_checksum(disk)
        print(disk)


def part2(filename):

    with open(filename) as f:
        disk = f.readline().strip()
        disk = gen_harddisk(disk)
        # print(disk)
        # root,tail = gen_disk2(disk)
        disk = compress2(disk)
        disk = calc_checksum(disk)
        print(disk)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = script_dir + "/example.txt"
    filename = script_dir + "/data.txt"

    # part1(filename)
    part2(filename)

if __name__ == "__main__":
    main()
