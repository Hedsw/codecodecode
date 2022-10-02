class Solution:
    # Hash Sep으로 접근
    # Time Comp - O(N^3)
    # Space Comp - O(N)
    # We iterate the combinations of nums[i], nums[j], nums[k], and calculate the last number by lastNumber = target - nums[i] - nums[j] - nums[k].
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):a
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans
    # Using DFS, 
    # Time compe O(NlogN+ N^(k-1))
    # Space - O(N)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(l, r, k, target, path, out):  # [l, r] inclusive
            if k == 2:
                while l < r:
                    if nums[l] + nums[r] == target:
                        out.append(path + [nums[l], nums[r]])
                        while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[l]
                        l, r = l + 1, r - 1
                    elif nums[l] + nums[r] > target:
                        r -= 1  # Decrease sum
                    else:
                        l += 1  # Increase sum
                return

            while l < r:
                dfs(l+1, r, k - 1, target - nums[l], path + [nums[l]], out)
                while l+1 < r and nums[l] == nums[l+1]: l += 1  # Skip duplicate nums[i]
                l += 1

        def kSum(k):  # k >= 2
            ans = []
            nums.sort()
            dfs(0, len(nums)-1, k, target, [], ans)
            return ans

        return kSum(4)