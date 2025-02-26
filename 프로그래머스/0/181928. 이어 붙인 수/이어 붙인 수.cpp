#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    string odd = "";
    string even = "";
    for (auto num: num_list) {
        if (num % 2 == 1) {
            odd += to_string(num);
        } else {
            even += to_string(num);
        }
    }
    
    // 짝수 홀수가 적어도 한 개씩 있으므로 빈 문자열일 경우는 없음
    return stoi(odd) + stoi(even);
    
    int answer = 0;
    return answer;
}