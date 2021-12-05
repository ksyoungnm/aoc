import numpy as np

def part1(file):
    
    nums = np.loadtxt(file,max_rows=1,delimiter=',',dtype=int)
    boards = np.loadtxt(file,skiprows=1,dtype=int)
    boards = np.reshape(boards, (-1,boards.shape[1],boards.shape[1]))
    
    mask = np.zeros(boards.shape, dtype=bool)
    winner = None

    for num in nums:
        mask = (boards == num) | mask
        # check cols
        if np.sum(np.sum(mask, axis=1) == 5) == 1:
            winner = np.where(np.sum(mask, axis=1) == 5)[0][0]
        #check rows
        if np.sum(np.sum(mask, axis=2) == 5) == 1:
            winner = np.where(np.sum(mask, axis=2) == 5)[0][0]
        
        if winner is not None:
            print(sum(boards[winner][~mask[winner]]) * num)
            break
        
#-------------------------------------------------------------------------------

def part2(file):

    nums = np.loadtxt(file,max_rows=1,delimiter=',',dtype=int)
    boards = np.loadtxt(file,skiprows=1,dtype=int)
    boards = np.reshape(boards, (-1,boards.shape[1],boards.shape[1]))
    
    mask = np.zeros(boards.shape, dtype=bool)
    prevwinners = set()
    winners = set()

    for num in nums:
        mask = (boards == num) | mask

        prevwinners = winners
        winners = winners.union(set(np.where(np.sum(mask, axis=1) == 5)[0]))
        winners = winners.union(set(np.where(np.sum(mask, axis=2) == 5)[0]))

        if len(winners) == boards.shape[0]:
            lastwinner = (winners - prevwinners).pop()
            print(sum(boards[lastwinner][~mask[lastwinner]]) * num)
            break
        
#-------------------------------------------------------------------------------

def main():
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()