#1.  Marks zero or negative numbers as positive numbers.
#2.Mark number x as visited by marking nums[x] as negative, by using (x-1) we can use index 0 of nums array.
#3. Interate from 0..n-1, if nums[i] > 0 then it means the number i+1 is the smallest positive number which is missing.

# Time Comp - O(N)
# Space COmp - O(N)
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        INF = n + 1
    
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = INF # marks zero or negative numbers as infinitive positive numbers
                
        for i in range(n):
            x = abs(nums[i]) - 1 # use index start with zero
            if x < n:
                nums[x] = -abs(nums[x]) # mark `x` as visited by marking `nums[x]` as negative
                    
        for i in range(n):
            if nums[i] > 0: # if nums[i] is positive -> number (i+1) is not visited.
                return i + 1
        return n + 1