
# There are two ways you can reverse a linked list, either iteratively or recursively.


class Solution:
    def reverse_iteratively(self, head):

        prev = None
        while prev:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return head

    def reverse_recursively(self, head):
        # this will reverse the nodes in the linked list for every recursive function call
        if not head or head.next:
            return head
        # this will one by one reverse the list by re-assigning the order.
        reversed_head = self.reverse_recursively(head.next)
        # 1 -> -> 2 -> 3 -> 4 ......... 5 -> 4
        head.next.next = head
        head.next = None

        return reversed_head


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


new_linked_list = Node(1)
new_linked_list.next = Node(2)
new_linked_list.next.next = Node(3)
new_linked_list.next.next.next = Node(4)
new_linked_list.next.next.next.next = Node(5)

new_solution = Solution()

reverse_head = new_solution.reverse_iteratively(new_linked_list)
print(reverse_head.val)
