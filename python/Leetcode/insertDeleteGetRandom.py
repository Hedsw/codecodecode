import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        #randomizeSet.remove(val)
        if val in self.pos:
            return False
        
        self.pos[val] = len(self.nums)
        
        self.nums.append(val)
        return True  

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        #randomizeSet.remove(val)
        # again, if the item is not in the data_map, return False. 
        # we check the dictionary instead of the list due to lookup complexity
        if not val in self.pos:
            return False
        
        # essentially, we're going to move the last element in the list 
        # into the location of the element we want to remove. 
        # this is a significantly more efficient operation than the obvious 
        # solution of removing the item and shifting the values of every item 
        # in the dicitionary to match their new position in the list
        
        """
        Here is the trick to remove in constant time.
        Assume that the order of elements does not matter.
        This is what you need to pay attention to.

        Suppose you have a vector (not indices, but actual values in those positions)

        0 1 2 3 4 5 6
        and you want to remove the value 3. You can turn this into

        0 1 2 6 4 5
        in O(1) without any issues. (Again assuming that we are not concerned about maintaining any             ordering, we are just looking to delete the value 3 in constant time)
        """        
        last_elem_in_list = self.nums[-1]
        index_of_elem_to_remove = self.pos[val]
        
        self.pos[last_elem_in_list] = index_of_elem_to_remove
        self.nums[index_of_elem_to_remove] = last_elem_in_list
        
        # change the last element in the list to now be the value of the element 
        # we want to remove
        self.nums[-1] = val
        
        # remove the last element in the list
        self.nums.pop()
        
        # remove the element to be removed from the dictionary
        self.pos.pop(val)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #return self.nums[random.randint(0, len(self.nums) - 1)]
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()