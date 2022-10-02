/*
1.Save all time points and the change on current meeting rooms.
2.Sort all the changes on the key of time points.
3.Track the current number of using rooms cur and update result res.

Time - O(NlogN)
Space - O(N)
*/
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> m;
        for(auto &t : intervals)
            m[t[0]]++, m[t[1]]--;
        
        int cur = 0, res = 0;
        for (auto &it: m)
            res = max(res, cur += it.second);
        return res;
    }
};