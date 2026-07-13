class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        j=k

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        a=nums[0] # Is supposed to be the first element in count but I don't know how to do that
        while j>0:
            
            for num in count:
                if count[num]>count[a]:
                    a = num
            output.append(a)
            count[a] = 0
            j -= 1

        return output