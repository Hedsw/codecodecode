// Time Comp - O(N)
// You are given several logs, where each log contains a unique ID and timestamp. 
// Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second,
// for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.
class LogSystem {
public:
    set<pair<string, int>> logs;
    unordered_map<string, int> idxs = {{"Year", 0}, {"Month", 1}, {"Day", 2}, {"Hour", 3}, {"Minute", 4}, {"Second", 5}};
    unordered_map<int, string> mins = {{0, ":00:00:00:00:00"}, {1, ":00:00:00:00"}, {2, ":00:00:00"}, {3, ":00:00"}, {4, ":00"}, {5, ""}};
    unordered_map<int, string> maxs = {{0, ":12:31:23:59:59"}, {1, ":31:23:59:59"}, {2, ":23:59:59"}, {3, ":59:59"}, {4, ":59"}, {5, ""}};
  
    LogSystem() {
        logs.clear();
    }
    
    void put(int id, string timestamp) {
        logs.insert({timestamp, id});
    }
    
    string getRange(string s, int idx, bool isStart) {
        int currIdx = 0;
        string res = "";
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (c == ':') {
                if (currIdx == idx) {
                    break;
                }
                else {
                    currIdx++;
                }
            }
            res += c ;
        }
        
        return isStart ? res + mins[idx] : res + maxs[idx];
    }
    
    vector<int> retrieve(string start, string end, string granularity) {
        int idx = idxs[granularity];
        
        string s = getRange(start, idx, true);
        string e = getRange(end, idx, false);
        
        auto itlow = logs.lower_bound({s, 0});
        vector<int> res;
        
        for(auto it = itlow; it != logs.end(); it++) {
            if(it->first > e) break;
            res.push_back(it->second);
        }
        return res;
    }
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem* obj = new LogSystem();
 * obj->put(id,timestamp);
 * vector<int> param_2 = obj->retrieve(start,end,granularity);
 */