#include <string>
#include <vector>
#include <iostream>

using namespace std;

int di[4] = {0, 1, 0, -1};  // 우하좌상
int dj[4] = {1, 0, -1, 0};

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer(n, vector<int>(n, 0));
    int i = 0; int j = 0;
    answer[i][j] = 1;
    int dir_idx = 0;
    while (answer[i][j] < n * n) {
        int ni = i + di[dir_idx];
        int nj = j + dj[dir_idx];
        if (0 <= ni && ni < n && 0 <= nj && nj < n && answer[ni][nj] == 0) {
            answer[ni][nj] = answer[i][j] + 1;
            i = ni; j = nj;
        } else {
            dir_idx = (dir_idx + 1) % 4;
        }
    }
    return answer;
}