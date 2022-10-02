// Use two hash tables to keep track of the friends relationship and the tweets, respectively. 
// For getting the news feed, first use a separate variable "time" to keep track of the time order when posting,
// then use a max heap to get the most recent ones, since the heap will do the sorting for us.

class Twitter {
private:
    int history=0;
    unordered_map<int, unordered_set<int>> following;
    unordered_map<int, vector<pair<int,int>>> tweets;
    //            user           history   tweetID
    
public:
    Twitter() { }
    
    void postTweet(int userId, int tweetId) {
        
        tweets[userId].push_back({history,tweetId});
        history++;
        
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> ans;
        priority_queue<pair<int,int>> pq;
        for(auto tweet : tweets[userId]){
            pq.push(tweet);
        }
        for(auto followee : following[userId]){
            for(auto tweet: tweets[followee]){
                pq.push(tweet);
            }
        }
        int sz = pq.size();
        int n = min(10,sz);
        for(int i=0; i<n;i++){
            int a = pq.top().second; pq.pop();
            ans.push_back(a);
        }
        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        
        following[followerId].insert(followeeId);
        
    }
    
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
        
        
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */