class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
         
        numb = len(digits)
        #print(numb)
        digit = 0
        for i in range(len(digits)):
            digit += 10 ** (len(digits)-i-1) * digits[i]
             
        #print(digit)
        digit = digit + 1
         
        digit = str(digit)
        return digit
