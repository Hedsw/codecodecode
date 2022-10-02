class Solution:

    def __init__(self, nums: List[int]):
        self.newNum = nums[:]
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.newNum

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.shuffled = self.newNum[:]
        random.shuffle(self.shuffled)
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()