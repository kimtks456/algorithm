#include <iostream>
#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int set_size, half{ (int)nums.size() / 2};
    set<int> s;
    
    for (int item : nums) {
        s.insert(item);
    }
   	
    set_size = s.size();
    
    answer = (set_size < half) ? set_size : half;
    
    return answer;
}