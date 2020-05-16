
# # This page represents two ways to do pre-order depth-first-search traversal
# # This can be done either recursively or iteratively


class Solution:
    # recursive solution
    def preorderTraversalRecursive(self, root):
        if not root:
            return []

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)

    # iterative solution
    def preorderTraversalIterative(self, root):
        if not root:
            return []

        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().preorderTraversalRecursive(root))
    print(Solution().preorderTraversalRecursive(root))
