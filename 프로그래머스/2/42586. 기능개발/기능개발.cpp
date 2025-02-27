#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> days(progresses.size());
    for (int i = 0; i < progresses.size(); i++) {
        int temp = 100 - progresses[i];
        if (temp % speeds[i] == 0) {
            days[i] = temp / speeds[i];
        } else {
            days[i] = temp / speeds[i] + 1;
        }
    }
    
    vector<int> answer;
    int func = 0;
    int cnt = 1;
    for (int i = 1; i < days.size(); i++) {
        if (days[i] > days[func]) {
            answer.push_back(cnt);
            func = i;
            cnt = 1;
        } else {
            cnt++;
        }
    }
    answer.push_back(cnt);
    return answer;
}