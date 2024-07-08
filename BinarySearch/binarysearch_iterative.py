from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                high = mid - 1

            else:
                low = mid + 1

        return -1


print(Solution().search([-1,0,3,5,9,12], 9))        # 4
