#include <string>
#include <vector>

using namespace std;

int answer = 0;

void make_target(int i, vector<int>& numbers, int target, int cur_num) {
    if (i == numbers.size()) {
        if (cur_num == target) answer++;
        return;
    }
    
    make_target(i + 1, numbers, target, cur_num + numbers[i]);
    make_target(i + 1, numbers, target, cur_num - numbers[i]);
}


int solution(vector<int> numbers, int target) {
    make_target(0, numbers, target, 0);
    return answer;
}