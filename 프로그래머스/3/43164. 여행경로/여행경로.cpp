#include <string>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

vector<bool> visited;
vector<string> answer;
bool flag;

void dfs(int cnt, string airport, vector<vector<string>>& tickets) {
    answer.push_back(airport);
    if (cnt == tickets.size()) {
        flag = true;
        return;
    }
    
    for (int i = 0; i < tickets.size(); i++) {
        if (!visited[i] && tickets[i][0] == airport) {
            visited[i] = true;
            dfs(cnt + 1, tickets[i][1], tickets);
            if (flag) return;
            answer.pop_back();
            visited[i] = false;
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    visited.resize(tickets.size(), false);
    sort(tickets.begin(), tickets.end());
    
    dfs(0, "ICN", tickets);
    return answer;
}