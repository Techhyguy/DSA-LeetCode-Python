class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)

        total = len(arr)
        k %= total

        arr = arr[-k:] + arr[:-k]

        ans = [[0] * n for _ in range(m)]

        idx = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = arr[idx]
                idx += 1

        return ans