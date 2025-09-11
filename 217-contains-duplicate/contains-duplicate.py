class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Store = set()

        for i in nums:
            if i in Store:
                return True
            else:
                Store.add(i)
        return False
            
        

        

