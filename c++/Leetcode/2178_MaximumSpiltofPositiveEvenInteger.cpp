class Solution {
public:
    vector<long long> maximumEvenSplit(long long s) {
        // Time: O(sqrt(N))
        // Space: O(sqrt(N))
        if (s % 2) return {};
        vector<long long> ans;
        function<bool(long, long)>dfs = [&](long i, long target) {
            if (target == 0) return true;
            if (target < i) return false;
            ans.push_back(i);
            if (dfs(i + 2, target - i)) return true; // use `i`
            ans.pop_back();
            return dfs(i + 2, target); // skip `i`
        };
        dfs(2, s);
        return ans;
    }

    // We can keep trying subtracting 2, 4, 6, 8, ... from finalSum. We stop the loop when subtracting the current number i is invalid -- s - i < i + 2 (the reminder after the subtraction is less than the next even number). And we push the reminder into the answer.
    vector<long long> maximumEvenSplit2(long long s) {
        if (s % 2) return {};
        vector<long long> ans;
        for (int i = 2; s - i >= i + 2; i += 2) {
            ans.push_back(i);
            s -= i;
        }
        ans.push_back(s);
        return ans;
    }


};