#include <string>
#include <vector>

using namespace std;

int dfs(vector<int>& nums, int depth, int now_sum, int target) {
	if (depth == nums.size()) {
        return now_sum == target;
    }
    
    return dfs(nums, depth + 1, now_sum + nums[depth], target)
    	+ dfs(nums, depth + 1, now_sum - nums[depth], target);
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, 0, 0, target);
}
