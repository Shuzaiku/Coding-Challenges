#include <vector>
#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> remains;
        for (int i = 0; i < nums.size(); i++) {
            remains[nums[i]] = i;
        }

        std::vector<int> indices;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int remain = target - num;
            if (remains.find(remain) != remains.end()) {
                if (remains[remain] != i) {
                    indices.insert(indices.end(), {i, remains[remain]});
                    break;
                }
            }
        }
        return indices;
    }
};
