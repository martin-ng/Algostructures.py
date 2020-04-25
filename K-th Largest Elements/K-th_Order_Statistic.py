# K-th order statistic is a classical textbook problem that involves looking for the K-th largest element in an array
# Following are commonly used solutions to solve this problem

import heapq


class Solution:
    # Sorting
    # O(nlogn) time, O(1) space
    def sorting(self, arr, k):
        arr.sort()
        return arr[len(arr)-k]

    # priority queue
    # O(nlogk) time, O(k) space
    def pq(self, arr, k):
        res = []
        for num in arr:
            if len(res) == k:
                heapq.heappushpop(res, num)
            else:
                heapq.heappush(res, num)
        return res[0]

    # quickselect
    # O(n) time average case, O(n^2) worst case, O(1) space
    def quickselect(self, arr, k):
        lo = 0
        hi = len(arr)-1
        k = len(arr)-k
        while lo <= hi:
            res = self.partition(arr, lo, hi)
            if res == k:
                print(arr[res])
                return arr[res]
            elif res > k:
                hi = res - 1
            else:
                lo = res + 1
        return res

    def partition(self, arr, lo, hi):
        pivot = lo
        while lo <= hi:
            while lo <= hi and arr[lo] <= arr[pivot]:
                lo += 1
            while lo <= hi and arr[hi] >= arr[pivot]:
                hi -= 1
            if lo > hi:
                break
            self.swap(arr, lo, hi)
        self.swap(arr, hi, pivot)
        return hi

    def swap(self, arr, left, right):
        arr[left], arr[right] = arr[right], arr[left]


# arr = [5, 2, 3, 9, 6, 8]
# arr = [1, 4, 3, 6, 8, 7]
arr = [2, 9, 3, 8, 5, 1]

new_solution = Solution()
# print(new_solution.pq(arr, 2))
print(new_solution.quickselect(arr, 3))
