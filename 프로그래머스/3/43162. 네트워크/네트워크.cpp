#include <string>
#include <vector>
#include <stack>

using namespace std;

void dfs(int s, vector<bool>& visited, vector<vector<int>>& computers) {
    stack<int> stk;
    stk.push(s);
    visited[s] = true;
    
    while (!stk.empty()) {
        int t = stk.top(); stk.pop();
        
        for (int i = 0; i < visited.size(); i++) {
            if (!visited[i] && computers[t][i] == 1) {
                visited[i] = true;
                stk.push(i);
            }
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    vector<bool> visited(n, false);
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, visited, computers);
            answer++;
        }
    }
    return answer;
}