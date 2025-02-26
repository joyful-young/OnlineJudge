#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> num_list) {
    int all_add = 0;
    int all_mul = 1;
    
    for (int i = 0; i < num_list.size(); i++) {
        all_add += num_list[i];
        all_mul *= num_list[i];
    }
    
    if (all_mul < all_add * all_add) {
        return 1;
    }
    return 0;
}