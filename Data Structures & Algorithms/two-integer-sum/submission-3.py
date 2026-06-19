class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashira = {}

        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in hashira:
                return [hashira[num2], index]
            hashira[num] = index

        return 0;