// 이전에는 LFU의 경우 Log(n)이 최선이였습니다. 그 이유는 Binomial Heap Implementation을 사용했기 때문입니다. 이 경우 Min Heap은 O(log n)이 되었기 떄문에 Heap을 사용한 방법은 O(log n)이 됩니다. 하지만 Professor Ketan은 2010년에 O(1) 방식으로 LFU를 설계할 수 있는 방법을 고안했습니다
// 그 방법은 Double-Linked List를 사용하는 방법입니다.
// 간단히 말해서, 그 방법은 Horrizontally 하나의 linked list를 구성하고,
// 나머지 하나의 Linked-List는 Vertically 구성하는 방법입니다. 

/*
E.g. Doubly linked list of (key,value) with frequency of 1 and 2:

freqMap[1] = (1,2) -> (3,6) -> (1,8) -> null
freqMap[2] = (2,2) -> (9,4) -> (7,8) -> null

*/

class LFUCache {
    unordered_map<int, list<pair<int, int>>> freqMap;
    unordered_map<int, pair<int, list<pair<int, int>>::iterator>> keyMap;
    int lowestFreq = 0;
    int cap;
    
public:
    LFUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if(keyMap.count(key)) {
            int val = (*(keyMap[key].second)).second;
            put(key, val);
            return val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(!keyMap.count(key)) {
            if(keyMap.size() < cap) {
                freqMap[1].emplace_back(key, value);
                keyMap[key] = {1, --freqMap[1].end()};
                lowestFreq = 1;
            }
            else {
                if(lowestFreq == 0) return;
                auto [k, v] = freqMap[lowestFreq].front();
                freqMap[lowestFreq].erase(freqMap[lowestFreq].begin());
                keyMap.erase(k);
                put(key, value);
            }
        }
        else {
            auto [freq, it] = keyMap[key];
            if (freqMap[freq].size() == 1 and freq == lowestFreq)
                lowestFreq++;
            freqMap[freq].erase(it);
            freqMap[freq+1].emplace_back(key, value);
            keyMap[key] = {freq+1, --freqMap[freq+1].end()};
        }
        
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */