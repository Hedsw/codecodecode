/*
Using two data structures here, an ordered map and a regular hashmap.

The ordered map is to make sure that we can get the maximum and minimum values in O(1), and I used a map to make sure that we can keep track of the count.

latestTime in combination with the prices hashmap also ensures that the current method is O(1).

The worst case for the update method is O(log N) due to the binary search in ordered to update price count (same time complexity if the timestamp already exists and you need to reduce prevPrice count).
*/
// Time Comp - O(logn), Space - O(n)
class StockPrice {
public:
    unordered_map<int, int> prices = {};
    map<int, int> ordered = {};
    int latestTime = -1;
    
    void update(int timestamp, int price) {
        if (prices.find(timestamp) != prices.end()) {
            int prevPrice = prices[timestamp];
            ordered[prevPrice]--;
            if (ordered[prevPrice] == 0)
                ordered.erase(prevPrice);
        }
        prices[timestamp] = price;
        ordered[price]++;
        latestTime = max(latestTime, timestamp);
    }
    
    int current() {
        return prices[latestTime];
    }
    
    int maximum() {
		// ordered.rbegin() means the first element in the map starting in reverse order, so the last element
		// this returns an iterator to a pair<int, int> in this case, where the second value of the pair is the count
		// and the first value is the price, and since its a pair from an iterator we access it with an arrow function: ->first
        return ordered.rbegin()->first;
    }
    
    int minimum() {
		// same logic as above, but this is an iterator that has the pair<int, int> values of the lowest price and its count
        return ordered.begin()->first;
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */