# Time Complexity - O(n) 왜냐면 For loop을 쓰니까 
# Space Complexity - O(n) 왜냐면.. Dict을 쓰니까

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Sort String first
        # check same string on length        
        ans = collections.defaultdict(list)
        
        for s in strs:

            tuples = tuple(sorted(s))
            print(tuples)
            ans[tuples].append(s)

        return list(ans.values())
            #Dictionary keys must be immutable types and list is a mutable type.
            # Tuple을 쓰는 이유는.. Dictionary에 넣을 때, Key가 변하면 안되는데 List는 변할 수 있음
            # 그래서 tuple을 사용하는 것.. tuple은 불변하는 것이라서 사용 가능함.        

    # Dictionary를 쓰면 Key Valu로 나뉘게 된다. 
    # 먼저 Sorting을 한 다음에, 그 Sorting한 문자를 기준으로, Key를 설정해두고
    # 각 Value들을 그 Key에 맞게 끼워 넣는다. 

    