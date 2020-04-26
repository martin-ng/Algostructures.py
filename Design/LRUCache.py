class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # set the boundaries for the doubly linked list so you do not have to worry about null objects
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return - 1
        current = self.map.get(key)
        self.moveToHead(current)
        return current.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            new_node = Node(key, value)
            self.addNode(new_node)
            self.map[key] = new_node
            if len(self.map) > self.cap:
                self.removeNode()

        else:
            current = self.map.get(key)
            current.key = key
            current.val = value
            self.moveToHead(current)
    # helper functions to easily add nodes after head and delete nodes before tail

    def addNode(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def removeNode(self) -> None:
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        del self.map[temp.key]

    def moveToHead(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
