#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_prefix) {
    for (int i = 1; i <= my_string.length(); i++) {
        if (my_string.substr(0, i) == is_prefix) return 1;
    }
    return 0;
}