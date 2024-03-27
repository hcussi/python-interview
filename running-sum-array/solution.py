from typing import List


class Solution:

    @staticmethod
    def running_sum(nums: List[int]) -> List[int]:
        result = []

        for idx, num in enumerate(nums):
            result.append(sum(nums[0:idx + 1]))

        return result
