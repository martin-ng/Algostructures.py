class Solution:

    # time complexity: O(N * N!) space complexity: O(N!)
    def permute(self, nums):
        if not nums:
            return []
        res = []
        visiting = set()
        self.permutate(0, nums, res, [], visiting)
        return res

    def permutate(self, index, nums, res, temp, visiting):
        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(nums)):
            if nums[i] in visiting:
                continue
            # we need to keep track of what we're visiting so we dont get duplicates
            visiting.add(nums[i])
            temp.append(nums[i])
            self.permutate(i + 1, nums, res, temp, visiting)
            temp.pop()
            visiting.remove(nums[i])


if __name__ == '__main__':
    Solution().permute([1, 2, 3])
    Solution().permute([4, 5, 6])
