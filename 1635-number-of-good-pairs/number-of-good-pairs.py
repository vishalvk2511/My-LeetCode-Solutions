class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c= 0

        for i,m in enumerate(nums):
            for j,n in enumerate(nums):
                if  nums[i] == nums[j] and i<j:
                    c+=1
        return c
        