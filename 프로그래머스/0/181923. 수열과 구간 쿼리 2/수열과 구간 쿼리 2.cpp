#include <string>
#include <vector>

using namespace std;

int find_ans(vector<int>& query, vector<int>& arr) {
    int ans = 1000001;
    for (int i = query[0]; i < query[1] + 1; i++) {
        if (arr[i] > query[2]) {
            ans = min(ans, arr[i]);
        }
    }
    return ans == 1000001 ? -1 : ans;
}

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer(queries.size());
    for (int i = 0; i < queries.size(); i++) {
        answer[i] = find_ans(queries[i], arr);
    }
    return answer;
}