#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> intStrs, int k, int s, int l) {
    vector<int> answer;
    for (const auto& elem: intStrs) {
        int intValue = stoi(elem.substr(s, l));
        if (intValue > k) answer.push_back(intValue);
    }
    return answer;
}