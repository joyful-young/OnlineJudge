#include<vector>
#include<queue>
using namespace std;

int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

int bfs(vector<vector<int>>& maps) {
    int n, m;
    n = maps.size();
    m = maps[0].size();
    
    vector<vector<int>> visited(n, vector<int>(m, -1));
    visited[0][0] = 1;
    queue<pair<int, int>> q(deque<pair<int, int>>{{0, 0}});
    
    while (!q.empty()) {
        auto [ti, tj] = q.front(); q.pop();
        
        for (int idx = 0; idx < 4; idx++) {
            int ni = ti + di[idx];
            int nj = tj + dj[idx];
            
            if (0 <= ni && ni < n && 0 <= nj && nj < m 
                && maps[ni][nj] == 1 && visited[ni][nj] == -1) {
                visited[ni][nj] = visited[ti][tj] + 1;
                q.push(make_pair(ni, nj));
            }
        }
    }
    return visited[n - 1][m - 1];
}

int solution(vector<vector<int>> maps) {
    return bfs(maps);
}