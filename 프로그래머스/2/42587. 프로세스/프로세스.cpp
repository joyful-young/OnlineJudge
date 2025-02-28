#include <string>
#include <vector>
#include <queue>

using namespace std;

int pr_value_cnt[10];

bool is_prior(int p) {
    for (int i = p + 1; i < 10; i++) {
        if (pr_value_cnt[i] > 0) return false;
    }
    return true;
}

int solution(vector<int> priorities, int location) {
    int n = priorities.size();
    queue<pair<int, int>> processes;
    for (int i = 0; i < n; i++) {
        pr_value_cnt[priorities[i]] += 1;
        processes.emplace(i, priorities[i]);
    }
    
    int answer = 1;
    while (answer <= n) {
        auto [l, p] = processes.front(); processes.pop();
        if (is_prior(p)) {
            // 가장 중요한 것이면 실행
            pr_value_cnt[p] -= 1;
            if (l == location) return answer;
            answer++;
        } else {
            // 더 중요한 게 남아있으면 다시 큐에 집어넣기
            processes.emplace(l, p);
        }
    }
    return answer;
}