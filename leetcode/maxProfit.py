class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices) #从图像上来看更好解决，最大盈利是吃到每一个波谷到波峰 
        if n <= 1:  
            return 0  
        count = 0  
        i = 1  
        while i != n:  
            diff = max((prices[i] - prices[i - 1]),0)  
            count += diff  
            i += 1  
        return count  
            
        
