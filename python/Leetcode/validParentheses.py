class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity - O(N^2) 그리고 Space - O(N) 왜냐하면 replace가 O(N)이고, While이 N인데 Loop니까.. N*N
        #It does not add additional space. It is in-place. So the string replacement is O(n) time. Also the while loop runs in O(n) making this algorithm O(n^2)
        if len(s) % 2 != 0:
            return False
        if len(s) < 2:
            return False
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return True if len(s) == 0 else False
    
    # Time Complexity is O(N), Space is O(N) 왜냐하면 Stack 하나에서 하기 때문... 
    #Complexity: time complexity is O(n): we put and pop each element of string from our stack only once. Space complexity is O(n).

    def isValid2(self, s):
        dct = {"[": "]", "(": ")", "{" : "}"}
        stack = []
        for char in s:
            if char in dct:
                stack.append(char)
            else:
                if not stack or char != dct[stack.pop()]: return False           
        return not stack

