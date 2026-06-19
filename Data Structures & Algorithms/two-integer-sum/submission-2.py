class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashira = {}

        for index, num in enumerate(nums):
            for i in hashira:
                if num + i == target:
                    return [hashira[i], index]
            hashira[num] = index

        return 0;