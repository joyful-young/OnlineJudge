#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int R, C;
int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> R >> C;
    vector<vector<char>> arr(R, vector<char>(C));
    
    pair<int, int> jihun;
    queue<pair<int, int>> fires;
    int MAX_TIME = 2000;
    vector<vector<int>> fire_map(R, vector<int>(C, MAX_TIME));
    vector<vector<int>> jihun_map(R, vector<int>(C, MAX_TIME));
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 'J') {
                jihun = {i, j};
                jihun_map[i][j] = 0;
            } else if (arr[i][j] == 'F') {
                fires.emplace(i, j);
                fire_map[i][j] = 0;
            }
        }
    }

    // 불 번짐 조사
    while (!fires.empty()) {
        auto [ti, tj] = fires.front(); fires.pop();

        for (int i = 0; i < 4; i++) {
            int ni = ti + di[i];
            int nj = tj + dj[i];

            if (0 <= ni && ni < R && 0 <= nj && nj < C 
                && fire_map[ni][nj] == MAX_TIME && arr[ni][nj] != '#') {
                fire_map[ni][nj] = fire_map[ti][tj] + 1;
                fires.emplace(ni, nj);
            }
        }
    }

    // 지훈 이동
    queue<pair<int, int>> q; q.push(jihun);
    while (!q.empty()) {
        auto [ti, tj] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int ni = ti + di[i];
            int nj = tj + dj[i];

            if (0 <= ni && ni < R && 0 <= nj && nj < C) {
                if (arr[ni][nj] != '#' && jihun_map[ni][nj] == MAX_TIME
                    && jihun_map[ti][tj] + 1 < fire_map[ni][nj]) {
                    jihun_map[ni][nj] = jihun_map[ti][tj] + 1;
                    q.emplace(ni, nj);
                }
            } else {
                cout << jihun_map[ti][tj] + 1 << "\n";
                return 0;
            }
        }
    }
    cout << "IMPOSSIBLE" << "\n";
    return 0;
}