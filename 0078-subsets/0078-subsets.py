class Solution:
    def subsets(self, nums):
        n = len(nums)
        answer = []

        for mask in range(1 << n):

            subset = []

            for i in range(n):

                if mask & (1 << i):
                    subset.append(nums[i])

            answer.append(subset)

        return answer