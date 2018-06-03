##Given an array of integers, return indices of the two numbers such that they add up to a specific target.
##You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        
        answer = [0,0] # initialize answer
        
        for i in range(l):
            mate = target - nums[i]
                   
            if mate in nums:
                if mate == nums[i] and nums.count(mate)==1: # only one elemenet and target = nums[i]*2
                    continue      
                else:
                    answer[0] = i
                    for j in range(i+1,l):
                        if nums[j] == mate:
                            answer[1]=j
                            return answer
