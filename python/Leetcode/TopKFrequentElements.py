class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        print(dic, "dic")
        sdic = sorted(dic, key = dic.get) # Dic을 dic.get을 기준으로 소팅하고, 그 결과를 리버스 시켜라 라는 뜻! 이때 key에는 함수만 들어가야함 
        print(sdic)
        # 거꾸로 리버스 시키고 싶을 땐,,, sorted(dic, key = dic.get, reversed = True)
        
        return sdic[-k:]
        
        