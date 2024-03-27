# Problem:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from solution import Solution


if __name__ == '__main__':

    solution = Solution.running_sum([1, 2, 3, 4])
    print(f'Solution: \n{solution}')
    solution = Solution.running_sum([])
    print(f'Solution: \n{solution}')
