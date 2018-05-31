class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(A)-1: ##此处索引一直更新所以不会超限
            if A[i] == A[i+1]:
                A.remove(A[i])
            else:
                i += 1
        return len(A)
    
    ## 此处的i 循环不更新，所以会索引超限
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                continue
            
        return len(nums)##
    
            
