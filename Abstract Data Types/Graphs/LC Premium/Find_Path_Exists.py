import collections

# Suppose you have a 2D array of binaries. 1 represent walls you cannot cross, 0 represents an open space. Determine if you can
# traverse from a starting point (0, 0) to the lower right portion of the map.
# This problem can be solved through DFS and BFS traversal. Implementations shown below also accounts for visited cells.

'''
    [
        [0, 0, 1, 1, 0], 
        [0, 1, 0, 0, 1], 
        [0, 0, 0, 1, 0], 
        [1, 0, 0, 0, 0]
    ]
        This should return True
'''

'''
    [
        [0, 0, 1, 1, 0], 
        [0, 1, 0, 0, 1], 
        [0, 1, 0, 1, 0], 
        [1, 0, 0, 0, 0]
    ]
        This should return False as you cannot reach the other side
'''

# Time complexity and space complexity for both solutions are O(m * n). M is the amount of rows, and N is the amount of columns.


def dfs(grid):
    visiting = set()

    def helper(i, j):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1:
            return False
        if grid[i][j] == 1 or (i, j) in visiting:
            return False
        if i == len(grid)-1 and j == len(grid[0]) - 1:
            return True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for u, v in directions:
            visiting.add((i, j))
            res = helper(i + u, j + v)
            if res:
                return True
        visiting.remove((i, j))
        return False

    return helper(0, 0)


def bfs(grid):
    m = len(grid)-1
    n = len(grid[0])-1
    queue = collections.deque([(0, 0)])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1)]

    while queue:
        x, y = queue.popleft()
        visited.add((x, y))

        if grid[x][y] == 1:
            continue
        if x == m and y == n:
            return True
        for u, v in directions:
            new_x = x + u
            new_y = y + v
            if new_x < 0 or new_x > m or new_y < 0 or new_y > n or (new_x, new_y) in visited:
                continue

            queue.append((new_x, new_y))

    return False


matrix = [[0, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0]]
# matrix = [[0, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0]]
# matrix = [[0, 0, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0]]


print(dfs(matrix))
print(bfs(matrix))
