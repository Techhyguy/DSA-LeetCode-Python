from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first():
            low = 0
            high = len(nums) - 1
            answer = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    answer = mid
                    high = mid - 1       # Search on left side

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return answer

        def find_last():
            low = 0
            high = len(nums) - 1
            answer = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    answer = mid
                    low = mid + 1        # Search on right side

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return answer

        return [find_first(), find_last()]