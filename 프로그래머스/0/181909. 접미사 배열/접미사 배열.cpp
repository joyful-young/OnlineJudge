#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(string my_string) {
    int l = my_string.length();
    vector<string> answer(l);
    for (int i = 0; i < l; i++) {
        answer[i] = my_string.substr(i, l - i);
    }
    sort(answer.begin(), answer.end());
    return answer;
}