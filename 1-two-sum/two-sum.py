class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        Store = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in Store:
                return [Store[diff],i]
            Store[nums[i]] = i
        