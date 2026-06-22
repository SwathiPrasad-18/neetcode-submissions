class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores: { value: index }
        prevMap = {} 
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in prevMap:
                # Returns the smaller index first because complement was seen earlier
                return [prevMap[complement], i]
                
            prevMap[num] = i