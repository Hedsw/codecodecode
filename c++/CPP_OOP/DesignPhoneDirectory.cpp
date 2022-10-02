// unordered_map 은 Hash Table로 구성되어 있고, 이는 Search Time이 O(1)
// Map은 Self balancing BST like Red-Black Tree, 이는 Search Time이 Log(n)

class PhoneDirectory {
private:
    unordered_set<int> pool;
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        for(int i=0; i < maxNumbers; i++) 
            pool.insert(i);
    }
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        if(pool.empty()) 
            return -1;
        int a = *pool.begin();
        pool.erase(a);
        return a; 
    }
    /** Check if a number is available or not. */
    bool check(int number) {
        return pool.count(number) > 0;
    }
    /** Recycle or release a number. */
    void release(int number) {
        pool.insert(number);
    }
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj->get();
 * bool param_2 = obj->check(number);
 * obj->release(number);
 */