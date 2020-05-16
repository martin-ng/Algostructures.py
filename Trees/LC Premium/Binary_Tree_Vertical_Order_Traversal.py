import collections


class Solution:

    # It is important to note that this problem does not ask for the values to be sorted
    # according to value. Order is based on the ordering from left to right respective to the row
    # This solution utilizes BFS traversal
    # Time complexity: O(n) as you are not sorting but using two variables to keep track of the rows
    # Space complexity: O(n) number of nodes in the tree
    def verticalOrder(self, root):
        if not root:
            return []

        order_map = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        lowest = highest = 0

        while queue:
            node, level = queue.popleft()

            if not node:
                continue
            order_map[level].append(node.val)
            lowest = min(lowest, level)
            highest = max(highest, level)

            queue.append((node.left, level - 1))
            queue.append((node.right, level + 1))

        return [order_map[num] for num in range(lowest, highest+1)]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().verticalOrder(root))
