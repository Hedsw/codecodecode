class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k in d:
            print(k)
            while num >= k:
                res += d[k]
                print(res)
                num -= k
        return res
    
    # Time and Space Complexity -> O(1), Because the while loop will go through the numerals list which is the constant size
    