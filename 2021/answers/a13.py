# this one was great, super cool way of reading out the answer. this solution
# relies heavily on the fact that the folds always happen in the exact middle
# of the paper

import numpy as np
    
def part1(file):
    with open(file) as f:
        points,folds = [l.split('\n') for l in f.read().split('\n\n')]
        points = [ tuple(map(int,p.split(','))) for p in points ]

        maxx = max(points,key=lambda x:x[0])[0]+1
        maxy = max(points,key=lambda x:x[1])[1]+1
        ffold = folds[0].split()[2].split('=')
        ffold[1] = int(ffold[1])
        ffold[0] = 0 if ffold[0] == 'y' else 1
        
        dots = np.zeros((maxx,maxy),dtype=bool)
        for p in points:
            dots[p] = True
    
        if ffold[0]:
            newdots = dots[:ffold[1],:] | dots[-1:ffold[1]:-1,:]
        else:
            newdots = dots[:,:ffold[1]] | dots[:,-1:ffold[1]:-1]
        print(np.sum(newdots))

#-------------------------------------------------------------------------------

def part2(file):
    with open(file) as f:
        points,folds = [l.split('\n') for l in f.read().split('\n\n')]
        points = [ tuple(map(int,p.split(','))) for p in points ]
        folds = [ tuple(f.split()[2].split('=')) for f in folds ]
        folds = [ (0 if f[0] == 'y' else 1, int(f[1])) for f in folds ]

        maxx = max((f for f in folds if f[0] == 1), key=lambda x:x[1])[1] * 2 + 1
        maxy = max((f for f in folds if f[0] == 0), key=lambda x:x[1])[1] * 2 + 1

        dots = np.zeros((maxx,maxy),dtype=bool)
        for p in points:
            dots[p] = True

        for ffold in folds:
            print(dots.shape, ffold)
            if ffold[0]:
                dots = dots[:ffold[1],:] | dots[-1:ffold[1]:-1,:]
            else:
                dots = dots[:,:ffold[1]] | dots[:,-1:ffold[1]:-1]

        pdots = np.full_like(dots, '.', dtype=str)
        pdots[dots] = '#'
        print(pdots.T)
    
#-------------------------------------------------------------------------------

def main():
    np.set_printoptions(linewidth=100000)
    filename = 'example.txt'
    filename = 'data.txt'
    # part1(filename)
    part2(filename)

if __name__ == '__main__':
    main()