// O(n) by two-pointers
class Solution {
public:
    int maxArea(vector<int>& height) {
        int size = height.size();        
        int left = 0, right = size - 1;
        int max_width = size - 1;
        int area = 0;
        for(auto width = max_width; width > 0; width--) {
            if (height[left] < height[right]) {
                area = max(area, width * height[left]);
                left += 1;   
            }
            else {
                area = max(area, width * height[right]);
                right -= 1;
            }
        }
        return area;
    }
};
