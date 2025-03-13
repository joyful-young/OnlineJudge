#include <iostream>
#include <queue>
#include <tuple>
#include <string>
#include <vector>

using namespace std;

int N, M, K;
vector<string> arr;
int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

int bfs(vector<string>& arr) {
    queue<tuple<int, int, int>> q;
    q.push({0, 0, 0});

    vector<vector<vector<int>>> visited(N, vector<vector<int>>(M, vector<int>(K + 1, 0)));
    visited[0][0][0] = 1;
    while (!q.empty()) {
        auto [xi, xj, k] = q.front(); q.pop();
        
        if (xi == N - 1 && xj == M - 1) {
            return visited[xi][xj][k];
        }

        for (int i = 0; i < 4; i++) {
            int ni = xi + di[i];
            int nj = xj + dj[i];

            if (ni < 0 || ni >= N || nj < 0 || nj >= M) {
                continue;
            }

            if (arr[ni][nj] == '0' && visited[ni][nj][k] == 0) {
                visited[ni][nj][k] = visited[xi][xj][k] + 1;
                q.push({ni, nj, k});
            } else if (arr[ni][nj] == '1' && k < K && visited[ni][nj][k + 1] == 0) {
                visited[ni][nj][k + 1] = visited[xi][xj][k] + 1;
                q.push({ni, nj, k + 1});
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> K;
    arr.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    cout << bfs(arr) << '\n';
}