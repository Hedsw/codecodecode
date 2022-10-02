class Solution:
    # Dynamic Programming
    # Time Complexity - O(Nlogn)
    # 
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        N = len(costs)//2
        minCost = 0
        for A, B in costs:
            refund.append(B - A)
            minCost += A
        refund.sort()
        for i in range(N):
            minCost += refund[i]
        return minCost
    # Let us first send all the people to the first city. Now, we need to choose half of them and change their city from first to second. Which ones we need to choose? Obviously the half with the smallest difference of costs between second and first cities. 
    # min_cost = cost_of_reaching_all_to_a + cost_of_reaching_to_b_subtracting_reaching_a
