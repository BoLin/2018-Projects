#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        lenth = len(nums)
        k= k%lenth

        for i in range(k):
            a = nums[lenth-1]
            nums.insert(0,a)
            nums.pop()
        
