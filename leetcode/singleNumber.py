class Solution:
    #Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i<len(nums):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] < nums[i+1]:
                 return nums[i]
            else:
                i+=2
                
