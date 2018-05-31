class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1: ##此处索引一直更新所以不会超限
            if nums[i] == nums[i+1]:
                A.remove(A[i])
            else:
                i += 1
        return len(nums)
    
    ## 如果用for loop会有问题，此处的i 循环不更新，所以会索引超限
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                continue
            
        return len(nums)##
    
            
