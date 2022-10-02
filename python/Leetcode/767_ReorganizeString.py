
#As there might be n pairs of tuple stores in the heap, and each push would take O(logn) time(tree height).
class Solution:
    def reorganizeString2(self, S: str) -> str:
        """
        Time Compe - O(Nlogn)
        Space Comp - O(N)
        """
        cnt = Counter(S)
        heap = [(-v,k) for k,v in cnt.items()]
        heapq.heapify(heap)
        ans = []
        while(len(heap)>1):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            ans.extend([x[1],y[1]])
            if x[0]<-1:
                heapq.heappush(heap,(x[0]+1,x[1]))
            if y[0]<-1:
                heapq.heappush(heap,(y[0]+1,y[1]))
        if heap:
            if heap[0][0]<-1:
                return "" # case where last left element count is more than 2
            ans.append(heap[0][1])
        return "".join(ans)


    """
    The idea is to build a max heap with freq. count
a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count immediately into the heap. Rather we store it in prev_a, prev_b variables.
c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b contains, has become eligible for next loop selection. so we add that back in the heap.

In Essence,

At each step, we make the currently added one ineligible for next step, by not adding it to the heap
at each step, we make the previously added one eligible for next step, by adding it back to the heap

    Time comp - O(N)
    Space Comp - O(26) because of Alphabet 
    """
    def reorganizeString(self, S):
        res, c = [], Counter(S)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(S): return ""
        return res
    
   