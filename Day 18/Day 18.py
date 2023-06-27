#%%
import numpy as np

def grid_init():
    with open('input.txt') as f:
        grid = [[*line.strip().replace('#','1').replace('.','0')] for line in f.readlines()]
    
    grid = np.array(grid).astype(int)
    return grid

def pad_grid(grid):
    padded_grid = np.c_[np.zeros(grid.shape[0]),grid, np.zeros(grid.shape[0])]
    padded_grid = np.vstack([np.zeros(padded_grid.shape[1]),padded_grid,np.zeros(padded_grid.shape[1])])

    return padded_grid

def faulty_corners(grid):
    grid[0,0] = 1
    grid[0,-1] = 1
    grid[-1,0] = 1
    grid[-1,-1] = 1

    return grid

def update_grid(grid):
    padded_grid = pad_grid(grid)
    new_grid = grid.copy()
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            pixel = grid[row,col]
            neighbors = padded_grid[row:row+3,col:col+3]
            neighbor_sum = np.sum(neighbors)

            if pixel == 1:

                if neighbor_sum - 1 not in [2,3]:
                    new_grid[row, col] = 0

            else:

                if neighbor_sum == 3:
                    new_grid[row, col] = 1
    
    return new_grid

def animate_grid(grid, steps, part2=False):
    if part2:
        grid = faulty_corners(grid)

    next_frame = grid.copy()
    for frame in range(steps):
        next_frame = update_grid(next_frame)
        if part2:
            next_frame = faulty_corners(next_frame)

    return next_frame

if __name__ == '__main__':
    starting_grid = grid_init()
    part1 = np.sum(animate_grid(starting_grid, 100, part2=False))
    part2 = np.sum(animate_grid(starting_grid, 100, part2=True))
# %%
