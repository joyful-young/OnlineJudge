#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string my_string, vector<int> index_list) {
    std::ostringstream oss;
    for (auto& idx: index_list) {
        oss << my_string[idx];
    }
    return oss.str();
}