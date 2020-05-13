class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        # sort the array if the input is not already sorted.
        # this solution relies on a sorted array.
        res = []
        self.recurse(0, candidates, res, target, [])
        return res

    def recurse(self, index, candidates, res, remain, temp):
        if remain < 0:
            return
        elif remain == 0:
            # it is very important to remember we're using one reference to the array so you have to
            # create a copy of it before appending it to our main array. Otherwise the numbers will be
            # overwritten
            res.append(temp[:])
            return
        for i in range(index, len(candidates)):
            temp.append(candidates[i])
            # we don't increment when recursing as we can have duplicate numbers in our solution
            self.recurse(i, candidates, res, remain - candidates[i], temp)
            temp.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([4, 5, 7, 9], 9))
