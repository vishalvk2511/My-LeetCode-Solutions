class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l= 0

        r = len(numbers)-1

        while l < r:
            summ = numbers[l] + numbers[r]
            
            if summ == target:
                return  [l + 1 , r + 1]
            
            if summ > target:
                r-=1
            else:
                l+=1
            

        