class Solution:
    # Time complexity - O(nlogn).
    # Space Complexity - O(n), to keep sorted intervals and answer.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort를 하는데, 리스트로 들어있는 놈을 리스트 안에서 첫번째 Element들의 순서에 맞게   Sort를 해라 라는 뜻 s
        intervals.sort(key = lambda x: x[0])
        answer = []
        
        for i in intervals:
            #print(i)
            # If Answer is empty
            if not answer:
                answer.append(i)
            
            # if Answer is not overlap 
            if answer[-1][-1] < i[0]:
                #print(i)
                answer.append(i)
            # if overlap, compare which one is bigger than another one.
            else:
                #print(answer[-1], i[-1])
                answer[-1][-1] = max(answer[-1][-1], i[-1])
        return answer
    
        # Time Complexity - O(nlogn)
        # Space Complexity - O(1), where Heap 
        def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
            minHeap = intervals # Heapify가 Time Complexity nlogN임 
            heapify(minHeap)  # Heapify in increasing by the starting time order
            ans = []
            while minHeap:
                start, end = heappop(minHeap)
                while minHeap and minHeap[0][0] <= end:
                    end = max(end, heappop(minHeap)[1])
                ans.append([start, end])
            return ans
