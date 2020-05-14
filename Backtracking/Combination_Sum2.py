class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.recurse(0, candidates, res, target, [], set())
        return res

    def recurse(self, index, candidates, res, remain, temp, visiting):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temp[:])
            return
        for i in range(index, len(candidates)):
            # this problem can't have duplicates. to handle these kind of situations
            # you simply iterate again if two contiguous elements are the same
            if i > index and candidates[i] == candidates[i-1]:
                continue
            temp.append(candidates[i])
            self.recurse(i+1, candidates, res, remain -
                         candidates[i], temp, visiting)
            temp.pop()


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
