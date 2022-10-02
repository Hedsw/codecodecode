class Solution:
    # Time Complexity - O(nlog(n)) but space complexity is O(1)
    def missingNumber(self, nums):
        sort = sorted(nums) # nlongn
        miss = 0
        for i in range(len(sort)+1): # 0 - 9
            if i != sort[i-1]:
                #print(i, sort[i-1])
                miss = i
        print(miss)
        return miss

    # Time Complexity - O(n) time, Space - O(1)
    def missingNumber2(self, nums):
        res = 0
        for i in range(len(nums)+1):
            res ^= i # ^ is XOR operator # res 에 처음꺼 넣고..
        for num in nums:
            res ^= num # res 에 두번째꺼 넣었을 때, Pair일 경우 0이 되고(XOR니까) 아닐 경우 숫자 남음
            # 그래서 그 한 숫자만 남은거 리턴하면 됨
        print(res)
        return res
    
    # Time Complexity - O(n) time, Space - O(1)
    #The idea is the following: let us sum all numbers between 1 and n and then 
    #subtract sum of all nums and in the end we will have exaclty number we need.
    def missingNumber3(self, nums):
        return len(nums)*(len(nums)+1)//2 - sum(nums)
        
    
if __name__ == '__main__':    
    sol = Solution()
    lists = [9,6,4,2,3,5,7,0,1]
    sol.missingNumber(lists)
    sol.missingNumber2(lists)

