class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flame = set()

        for i in nums:
            if i in flame:
                return True
            else:
                flame.add(i)
        
        return False