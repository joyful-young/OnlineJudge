#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    // 1.
    int n = board.size();
    
    // 2.
    int count = 0;
    
    // 3.
    int dh[] = {0, 1, -1, 0};
    int dw[] = {1, 0, 0, -1};
    
    // 4.
    for (int i = 0; i < 4; i++) {
        int h_check = h + dh[i];
        int w_check = w + dw[i];
        if (0 <= h_check && h_check < n && 0 <= w_check && w_check < n) {
            if (board[h][w] == board[h_check][w_check]) count++;
        }
    }
    
    return count;
}