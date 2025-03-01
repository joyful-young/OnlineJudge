#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> cards) {
    int n = cards.size();
    vector<bool> visited(n, false);
    vector<int> cnts;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            int cnt = 1;
            
            int card = cards[i] - 1;
            while (!visited[card]) {
                cnt += 1;
                visited[card] = true;
                card = cards[card] - 1; 
            }
            cnts.push_back(cnt);
        }
    }
    if (cnts.size() < 2) {
        return 0;
    } else {
        sort(cnts.rbegin(), cnts.rend());
        return cnts[0] * cnts[1];
    }
}