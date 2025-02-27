#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> stk;
    for (int num: arr) {
        if (stk.empty() || stk[stk.size() - 1] != num) {
            stk.push_back(num);
        }
    }
    return stk;
}