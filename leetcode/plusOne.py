##Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

##The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

##You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0,0)
        l = len(digits) 
                
        for i in reversed(range(l)):
            if digits[i]+1<=9 :
                digits[i] +=1
                break
            else:
                digits[i]=0
        
        if digits[0]==0:
            digits.remove(0)
            
        return digits
            
