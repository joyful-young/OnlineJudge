#include <string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s) {
    stack<char> stk;
    bool answer = true;
    
    for (char c: s) {
        if (c == '(') {
            stk.push(c);
            continue;
        }
        
        if (stk.empty()) return false;
        stk.pop();
    }
    return stk.empty();
}