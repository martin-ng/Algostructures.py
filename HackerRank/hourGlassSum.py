# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    m = len(arr)
    n = len(arr[0])

    max_sum = float('-inf')

    for i in range(1, m-1):
        for j in range(1, n-1):
            max_sum = max(max_sum, sumHourGlass(arr, i, j))

    return max_sum


def sumHourGlass(grid, row, col):
    hourglass_arr = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]

    total_sum = 0
    for r, c in hourglass_arr:
        new_r = r + row
        new_c = c + col
        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
            return 0
        total_sum += grid[new_r][new_c]
    return total_sum + grid[row][col]
