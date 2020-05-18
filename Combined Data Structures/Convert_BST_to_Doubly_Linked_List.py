
class Solution:
    # this problem asks you to convert a binary search tree into a doubly linked list
    # you can do in order traversal, either recursively or iteratively and make the list as you iterate
    # time complexity O(n), space complexity O(n)
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        stack = []
        node = root
        dummy_head = Node(0)
        curr = dummy_head
        curr_behind = curr

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                curr.right = Node(node.val)
                curr.right.left = curr_behind

                curr_behind = curr.right
                curr = curr.right
                node = node.right

        curr_behind.right = dummy_head.right
        dummy_head.right.left = curr_behind

        return dummy_head.right


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    node_one = Node(1)

    node_two = Node(2)

    node_three = Node(3)

    node_four = Node(4)

    node_five = Node(5)

    node_one.right = node_two
    node_two.left = node_one
    node_two.right = node_three
    node_three.right = node_four
    node_four.right = node_five
    node_five.right = node_one
    node_three.left = node_two
    node_four.left = node_three
    node_five.left = node_four

    start = node_one

    print(Solution().treeToDoublyList(start))
