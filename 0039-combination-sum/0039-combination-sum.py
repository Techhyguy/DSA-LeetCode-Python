class Solution:
    def combinationSum(self, candidates, target):

        result = []
        path = []

        def dfs(index, remaining):

            # Found one valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # Invalid path
            if remaining < 0 or index == len(candidates):
                return

            # Take current element
            path.append(candidates[index])
            dfs(index, remaining - candidates[index])
            path.pop()

            # Skip current element
            dfs(index + 1, remaining)

        dfs(0, target)

        return result