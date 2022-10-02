

#We count the frequency of each char in the string and push to a max heap with count as priority key. We want to use a maxHeap because we need to process the most frequent char first in order to allow the greatest distant apart for each char.
#Use a hashmap as a 'waitlist' where key is i+k. When an item is avaialble at i in waitlist, it is ready to be pushed back into the maxHeap. This fulfills the requirement of the same char being at least k distance apart
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # If k is 0 we don't need to rearrange
        if k == 0: return s
        
        res = [''] * len(s)
        
        maxHeap = []
        waitList = {}
        
        # Get the count of each char and push to a maxHeap
        count = collections.Counter(s) # O(n)
        for char, count in count.items(): # O(log26)
            heappush(maxHeap, (count * -1 ,char))

        # O(n)
        for i in range(len(s)):
            # Check the waitlist if a char is ready to be added
            if waitList.get(i):
                heappush(maxHeap, (waitList[i][0], waitList[i][1]))
                del waitList[i]

            # If maxHeap is empty then the next char in waitList is unreachable and cannot fulfull requirement so we return empty string
            if not maxHeap: return ""
            count , char = heappop(maxHeap)
            res[i] = char
            count += 1 # Increment here cus we're using a maxHeap, value is negated
            if count < 0:
                # Add to waitlist with i + k (next index this char can be added again) as key
                waitList[i+k] = (count, char)

        return "".join(res)