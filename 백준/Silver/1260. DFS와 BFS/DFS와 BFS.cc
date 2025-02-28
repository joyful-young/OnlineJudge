#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

int N, M, V;

vector<int> dfs(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size() + 1, false);
    stack<int> stk; stk.push(start);

    int t;
    vector<int> ans;
    while (!stk.empty()) {
        t = stk.top(); stk.pop();

        if (!visited[t]) {
            visited[t] = true;
            ans.push_back(t);

            for (auto it = graph[t].rbegin(); it != graph[t].rend(); it++) {
                stk.push(*it);
            }
        }
    }
    return ans;
}

vector<int> bfs(vector<vector<int>>& graph, int start) {
    vector<bool> visited(graph.size() + 1, false);
    queue<int> q; q.push(start);
    visited[start] = true;

    int t;
    vector<int> ans = {start};
    while (!q.empty()) {
        t = q.front(); q.pop();

        for (const auto& n: graph[t]) {
            if (!visited[n]) {
                visited[n] = true;
                ans.push_back(n);
                q.push(n);
            }
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> V;
    vector<vector<int>> graph(N + 1);
    int s, e;
    while (M--) {
        cin >> s >> e;
        graph[s].push_back(e);
        graph[e].push_back(s);
    }
    for (int i = 1; i < N + 1; i++) {
        sort(graph[i].begin(), graph[i].end());
    }
    auto dfs_rlt = dfs(graph, V);
    for (const auto& x: dfs_rlt) {
        cout << x << " ";
    }
    cout << "\n";
    auto bfs_rlt = bfs(graph, V);
    for (const auto& x: bfs_rlt) {
        cout << x << " ";
    }
}