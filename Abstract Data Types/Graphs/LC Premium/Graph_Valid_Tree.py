class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # can use either a hash tasble or a list for adjacency list
        # neighbors = {i: [] for i in range(n)}
        neighbors = [[] for i in range(n)]
        visited = set()
        parent = {0: -1}

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        stack = [0]
        visited = set()
        visited.add(0)

        while stack:
            curr = stack.pop()
            for neighbor in neighbors[curr]:
                if neighbor == parent[curr]:
                    continue
                if neighbor in parent:
                    return False
                stack.append(neighbor)
                parent[neighbor] = curr

        return len(parent) == n


n = 5
arr = [[0, 1], [0, 2], [0, 3], [1, 4]]
# returns True

n = 5
arr = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# return False
