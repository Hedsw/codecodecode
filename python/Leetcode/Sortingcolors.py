# three pointer
def sortColors(self, nums):
    left, mid, right = 0, 0, len(nums)-1 # left points 0, mid points 1, right points 2
    while mid <= right:
        if mid > left and nums[mid] == 0: # mid encounter 0, need to swap with left // mid가 left보다 오른쪽에 위치하고, nums[mid]가 0인거
            nums[mid], nums[left] = nums[left], nums[mid]
            # mid doesn't change, increament left
            left += 1
        elif nums[mid] == 2: # mid encounter 2, need to swap with right //nums[mid] 가 2일 경우, 정상 위치이니, 올바른 위치에 있으니 right - 1 시킴
            nums[mid], nums[right] = nums[right], nums[mid]
            # mid doesn't change, decreament right
            right -= 1
        else: # mid encounter 1, correct position # mid가 중간에 있을 경우, 정상 위치이니.. +1 시킴
            mid += 1
"""
This problem is called Dutch national flag problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

The idea here is the following: we keep 3 pointers: for each of colors (numbers). I called them
beg = 0, mid = 0, end = len(nums) - 1. The idea here is to put sorted 0 and 1 to the beginning and sorted 2s to the end. Then we iterate over all elements and process each new element in the following way. Imagine, that we already sorted some of the elements, our invariant will be 00...0011...11......22....22, where we already put some 0 and 1 in the beggining and some 2 to the end. Then there are 3 possible optinos for new element ?:

00...0011...11?......22....22, where ? = 1, then we do not need to change any elements, just move mid pointer by 1 to the right.
00...0011...11?......22....22, where ? = 2, then we need to put this element befor the first already sorted 2, so we change these elements and then move pointer end by 1 to the left.
00...0011...11?......22....22, where ? = 0, then we need to swap this element with the last sorted 0 and also move two pointers mid and beg by 1.
We can see it this way, that pointers beg, mid and end always point at elements just after the last 0, after the last 1 and before the first 2.

Complexity: Time complexity is O(n), because each moment of time we move at least one of the pointers. Additional space complexity is O(1): to keep only 3 variables: beg, mid and end.
"""
# Since the vars red, white, blue increase with the size of nums, the space complexity is O(log(n)).

left, mid, right = 0, 0, len(nums) - 1

while mid <= right:
    if mid > left and nums[mid] == 0: # mid > left and nums[mid] == 0
        nums[mid], nums[left] = nums[left], nums[mid]
        
        left += 1
        
    elif nums[mid] == 2:
        nums[mid], nums[right] = nums[right], nums[mid]
        
        right -= 1
    else: # Encounter == 1
        mid += 1