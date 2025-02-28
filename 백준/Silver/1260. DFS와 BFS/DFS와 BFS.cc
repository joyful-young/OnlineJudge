#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

void dfs(vector<vector<int>>& graph, vector<int>& visited, int v) {
    stack<int> stk; stk.push(v);
    while (!stk.empty()) {
        v = stk.top(); stk.pop();
        if (!visited[v]) {
            visited[v] = true;
            cout << v << " ";

            for (auto it = graph[v].rbegin(); it != graph[v].rend(); it++) {
                stk.push(*it);
            }
        }
    }
}

void bfs(vector<vector<int>>& graph, vector<int>& visited, int v) {
    queue<int> q; q.push(v);
    visited[v] = true;
    cout << v << " ";
    
    while (!q.empty()) {
        v = q.front(); q.pop();

        for (const auto& w: graph[v]) {
            if (!visited[w]) {
                visited[w] = true;
                q.push(w);
                cout << w << " ";
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, V;
    cin >> N >> M >> V;

    // 인접행렬
    vector<vector<int>> adjL(N + 1);
    int v, w;
    while (M--) {
        cin >> v >> w;
        adjL[v].push_back(w);
        adjL[w].push_back(v);
    }
    for (int i = 1; i < N + 1; i++) {
        sort(adjL[i].begin(), adjL[i].end());  // 오름차순 정렬
    }

    vector<int> visited(N + 1, false);
    dfs(adjL, visited, V);
    cout << "\n";
    
    fill(visited.begin(), visited.end(), false);
    bfs(adjL, visited, V);
    return 0;
}