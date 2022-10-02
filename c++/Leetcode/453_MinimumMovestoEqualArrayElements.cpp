/*
Take the minimum number from the array and then substarct that minimum number from all the elements in the array, the final answer is the sum of the difference between the minimum number and the integer values in the given array.
For example:
if the given array is [5,6,7,8] then the minimum value is 5. Substracting it from all the values given in the array will give us 5-5 + 6-5 + 7-5 + 8-5 =0 + 1 + 2 + 3 = 6.
*/
// Time Comp - O(N)
class Solution {
public:
    int minMoves(vector<int>& nums) {
        int m=INT_MAX;
        for(int n:nums) m = min(m,n);
        int ans=0;
        for(int n:nums) ans+=n-m;
        return ans;

    }
};