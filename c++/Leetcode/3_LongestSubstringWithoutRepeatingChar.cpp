/* Sliding Window Problem
Time Complexity O(N)
Space Complexity O(k)
[k = length of the longest substring w/o repeating characters]
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        auto n = s.size();
        auto l = 0;
        auto r = n - 1;
        
        unordered_set<char> visited;
        
        auto maxStr = 0;
        for(auto r = 0; r < n; r++) {
            if(visited.find(s[r]) == visited.end()) {
                visited.insert(s[r]);
                maxStr = max(maxStr, r-l+1);
                
            }
            else {
                while(l != r && s[l] != s[r])
                    visited.erase(s[l++]);
                
                visited.erase(s[l++]);
                visited.insert(s[r]);
                
                maxStr = max(maxStr, r-l+1);
                
            }
        }
        
        return maxStr;
        
    }
};