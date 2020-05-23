import heapq

# this code will form a heap for a series of lists. the purpose of the iterator is to pop and return the minimum everytime
# next is called


class Solution:
    # time complexity O(n) to create the heap, O(logn) to return the next minimum
    def __init__(self, list1, list2, list3):
        self.heap = []

        if list1:
            list1.sort()
            for i in range(len(list1)):
                heapq.heappush(self.heap, list1[i])
        if list2:
            list2.sort()
            for i in range(len(list2)):
                heapq.heappush(self.heap, list2[i])
        if list3:
            list3.sort()
            for i in range(len(list2)):
                heapq.heappush(self.heap, list3[i])

        print(self.heap)

    def has_next(self):
        return self.heap

    def next(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return


if __name__ == "__main__":

    list1 = [5, 1, 2, 4]
    list2 = [4, 6, 3]
    list3 = [9, 0, 7]

    sorted_iterator = Solution(list1, list2, list3)
    print(sorted_iterator.has_next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
    print(sorted_iterator.next())
