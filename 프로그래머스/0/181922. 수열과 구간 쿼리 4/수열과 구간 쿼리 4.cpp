#include <string>
#include <vector>

using namespace std;

void process_query(vector<int>& query, vector<int>& arr) {
    for (int i = query[0]; i <= query[1]; i++) {
        if (query[2] == 0 || i % query[2] == 0) arr[i] += 1;
    }
}

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    for (auto query: queries) {
        process_query(query, arr);
    }
    return arr;
}