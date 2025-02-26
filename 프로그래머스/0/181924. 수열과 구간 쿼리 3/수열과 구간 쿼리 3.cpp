#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    for (const auto& query: queries) {
        swap(arr[query[0]], arr[query[1]]);
    }
    return arr;
}