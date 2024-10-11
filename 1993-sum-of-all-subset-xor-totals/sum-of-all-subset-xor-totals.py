class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total, n = 0, len(nums)
        for mask in range(1 << n):
            s = 0
            for i in range(n):
                if mask >> i & 1:
                    s ^= nums[i]
            total += s
        return total